const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const tick = () => new Promise(resolve => setImmediate(resolve));
const deferred = () => {
  let resolve, reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return {promise, resolve, reject};
};
const data = marker => ({
  marks: {beforeEnd: [55], phi: [marker], potential: [1]},
  phi: [marker], potential: [1], n: [marker], eps1: [.01], eps2: [.02], epsV: [.01], eps2V: [.02],
});

async function harness() {
  const nodes = new Map(), pending = new Map(), draws = [];
  let select, holdPlot = null;
  const get = id => {
    if (!nodes.has(id)) nodes.set(id, {
      id, hidden: true, value: 'power', setAttribute() {}, addEventListener() {},
      getClientRects() { return [1]; },
    });
    return nodes.get(id);
  };
  const window = {
    slowRollView: 'background', plotReady: Promise.resolve(), innerWidth: 1000,
    addEventListener() {}, dispatchEvent() {},
    SlowRollUI: {
      locale: 'en', t: {}, typeset: async () => {},
      load: key => {
        const request = deferred();
        pending.set(key, request);
        return request.promise;
      },
      selectors: (a, b, c, callback) => { select = callback; return () => 'starobinsky'; },
    },
  };
  const document = {
    documentElement: {dataset: {}}, getElementById: get,
    querySelectorAll: () => [], querySelector: () => ({}),
  };
  const Plotly = {
    react: async (element, traces) => {
      const gate = holdPlot;
      holdPlot = null;
      if (gate) await gate.promise;
      draws.push({id: element.id, marker: traces[0].x[0]});
    },
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../static/supporting.js'), 'utf8'), {
    window, document, Plotly, Event: class {}, setTimeout, clearTimeout,
  });
  await tick();
  return {select, pending, draws, get, hold: gate => { holdPlot = gate; }};
}

test('a delayed older response cannot replace the selected model', async () => {
  const h = await harness();
  h.select('phi2');
  h.pending.get('background-phi2').resolve(data(2));
  await tick();
  h.pending.get('background-starobinsky').resolve(data(1));
  await tick();
  assert.deepEqual(h.draws.map(d => d.marker), [2, 2]);
});

test('a stale failure does not show an error for a successful newer selection', async () => {
  const h = await harness();
  h.select('phi2');
  h.pending.get('background-phi2').resolve(data(2));
  await tick();
  h.pending.get('background-starobinsky').reject(new Error('older request failed'));
  await tick();
  assert.equal(h.get('support-error').hidden, true);
  assert.equal(h.draws.at(-1).marker, 2);
});

test('a slow earlier Plotly render finishes before the newer render', async () => {
  const h = await harness(), gate = deferred();
  h.hold(gate);
  h.pending.get('background-starobinsky').resolve(data(1));
  await tick();
  h.select('phi2');
  h.pending.get('background-phi2').resolve(data(2));
  await tick();
  gate.resolve();
  await tick();
  assert.deepEqual(h.draws.slice(-2).map(d => d.marker), [2, 2]);
  assert.equal(h.get('support-error').hidden, true);
});
