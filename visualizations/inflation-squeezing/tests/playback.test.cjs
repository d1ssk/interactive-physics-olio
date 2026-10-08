// Run with: node --test visualizations/inflation-squeezing/tests/playback.test.cjs
const assert = require('node:assert/strict');
const {readFileSync} = require('node:fs');
const path = require('node:path');
const {test} = require('node:test');
const vm = require('node:vm');

const settle = () => new Promise(resolve => setImmediate(resolve));

async function application(filename) {
  const nodes = new Map(), frames = new Map(), timers = new Map(), renders = [];
  let serial = 0;
  function node(id) {
    if (!nodes.has(id)) nodes.set(id, {
      value: id === 'speed' ? '1' : '0', style: {}, dataset: {}, listeners: {},
      setAttribute() {}, appendChild() {},
      addEventListener(type, handler) { this.listeners[type] = handler; },
    });
    return nodes.get(id);
  }
  const payload = filename === 'app.js' ? {
    limit: 5, grid: [],
    frames: Array.from({length: 8}, (_, i) => ({
      x: 12 - i, n: i, r: i, angle: 0, fields: [[], [], []], ring: [],
      markers: Array.from({length: 12}, () => [0, 0]),
    })),
  } : {
    acoustic: {
      u: [0, 1, 2, 3, 4],
      coherent: {curves: [], power: [], exact: []},
      incoherent: {curves: [], power: [], exact: []},
    },
  };
  const context = {
    URLSearchParams, location: {search: '?lang=en'}, Event: class {},
    document: {
      documentElement: {dataset: {}}, hidden: false,
      getElementById: node, querySelector: node, querySelectorAll: () => [],
      createElementNS: () => node(`svg-${serial++}`), addEventListener() {},
    },
    window: {inflationView: 'acoustic', innerWidth: 1000, plotReady: Promise.resolve(),
      addEventListener() {}, dispatchEvent() {}},
    MathJax: {startup: {promise: Promise.resolve()}, typesetClear() {},
      typesetPromise: () => Promise.resolve()},
    Plotly: {react: () => Promise.resolve(), relayout: () => new Promise(resolve => renders.push(resolve))},
    fetch: async () => ({ok: true, json: async () => payload}),
    performance: {now: () => 0},
    requestAnimationFrame: callback => { const id = ++serial; frames.set(id, callback); return id; },
    cancelAnimationFrame: id => frames.delete(id),
    setTimeout: callback => { const id = ++serial; timers.set(id, callback); return id; },
    clearTimeout: id => timers.delete(id),
  };
  context.window.MathJax = context.MathJax;
  vm.runInNewContext(readFileSync(path.join(__dirname, '../static', filename), 'utf8'), context);
  await settle();
  return {
    node, frames, timers,
    click: id => node(id).listeners.click(),
    input: (id, value) => { node(id).value = String(value); node(id).listeners.input(); },
    finishRender: async () => {
      // Each cursor update awaits three independently rendered plots.
      assert(renders.length >= 3);
      renders.splice(0, 3).forEach(resolve => resolve());
      await settle();
    },
  };
}

function fire(queue, time) {
  const callbacks = [...queue.values()];
  queue.clear();
  callbacks.forEach(callback => callback(time));
}

test('main animation keeps one frame chain across rapid pause/restart and reset', async () => {
  const app = await application('app.js');
  for (let i = 0; i < 5; i++) {
    app.click('play');
    assert.equal(app.frames.size, 1);
    app.click('play');
    assert.equal(app.frames.size, 0);
  }
  app.click('play');
  fire(app.frames, 65);
  assert.equal(Number(app.node('time').value), 1);
  assert.equal(app.frames.size, 1);
  app.click('reset');
  assert.equal(app.frames.size, 0);
  assert.equal(Number(app.node('time').value), 0);
  app.click('play');
  app.input('time', 3);
  assert.equal(app.frames.size, 0);
  assert.equal(Number(app.node('time').value), 3);
});

test('an acoustic render pending at pause cannot schedule work in a restarted run', async () => {
  const app = await application('supporting.js');
  app.click('acoustic-play'); // Run 1 awaits Plotly at index 1.
  app.click('acoustic-play'); // Stop, with no timer yet to clear.
  app.click('acoustic-play'); // Run 2 awaits Plotly at index 2.
  assert.equal(Number(app.node('acoustic-time').value), 2);
  await app.finishRender(); // Run 1 finishes after run 2 has started.
  assert.equal(app.timers.size, 0);
  assert.equal(app.node('acoustic-play').textContent, 'Pause');
  await app.finishRender();
  assert.equal(app.timers.size, 1);
  fire(app.timers);
  assert.equal(Number(app.node('acoustic-time').value), 3);
  app.input('acoustic-time', 0); // Scrub while the step is awaiting Plotly.
  await app.finishRender();
  assert.equal(app.timers.size, 0);
  assert.equal(Number(app.node('acoustic-time').value), 0);
  await app.finishRender();
  assert.equal(app.node('acoustic-play').textContent, 'Play');
});

test('an old final-frame render cannot stop a new acoustic playback run', async () => {
  const app = await application('supporting.js');
  app.input('acoustic-time', 3);
  await app.finishRender();
  app.click('acoustic-play'); // Pending final frame.
  app.click('acoustic-play');
  app.click('acoustic-play'); // Restart at the beginning.
  await app.finishRender();
  assert.equal(app.node('acoustic-play').textContent, 'Pause');
  assert.equal(app.timers.size, 0);
  await app.finishRender();
  assert.equal(app.timers.size, 1);
  assert.equal(Number(app.node('acoustic-time').value), 1);
});
