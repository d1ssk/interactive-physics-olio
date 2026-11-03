import assert from 'node:assert/strict';
import test from 'node:test';
import '../src/physics_atlas/static/figure-data.js';
const {unpack, createStore, createPanel} = globalThis.PhysicsFigureData;
const packed = {format: 1, pool: [[1.2345678901234567, -0, null]], root: [{'$ref': 0}, {'$ref': 0}]};

test('unpacking preserves numbers and gives independent mutable arrays', () => {
  const result = unpack(packed);
  assert.deepEqual(result, [packed.pool[0], packed.pool[0]]);
  result[0][0] = 5;
  assert.equal(result[1][0], 1.2345678901234567);
  assert(Object.is(result[1][1], -0));
  assert.throws(() => unpack({format: 1, pool: [{'$ref': 0}], root: {'$ref': 0}}));
});

test('concurrent and repeated requests share one fetch; failures can be retried', async () => {
  let requests = 0;
  const urls = [];
  const store = createStore({chunks: {a: 'part.hash.json'}}, 'https://example.org/project/topic/figure-data/', async url => {
    urls.push(String(url));
    requests++;
    if (requests === 1) return {ok: false, status: 503};
    return {ok: true, json: async () => packed};
  });
  const a = store.load('a'), b = store.load('a');
  assert.equal(a, b);
  await assert.rejects(a);
  assert.equal(store.has('a'), false);
  await Promise.all([store.load('a'), store.load('a')]);
  await store.load('a');
  assert.equal(requests, 2);
  assert.equal(store.has('a'), true);
  assert.equal(urls[0], 'https://example.org/project/topic/figure-data/part.hash.json');
  await assert.rejects(store.load('unknown'));
});

function panel(locale = 'en') {
  const text = {}, button = {addEventListener(type, fn) { this.click = fn; }};
  const status = {querySelector(selector) { return selector === 'button' ? button : text; }};
  const element = {querySelector() { return status; }, setAttribute(key, value) { this[key] = value; }};
  const slider = {};
  return {controller: createPanel(element, [slider], locale), element, slider, status, text, button};
}
const deferred = () => { let resolve; const promise = new Promise(r => { resolve = r; }); return {promise, resolve}; };

test('a stale response cannot replace the latest selection or change its loading state', async () => {
  const ui = panel();
  const old = deferred(), recent = deferred();
  const rendered = [];
  const first = ui.controller.run(async current => { await old.promise; if (current()) rendered.push('old'); });
  const second = ui.controller.run(async current => { await recent.promise; if (current()) rendered.push('recent'); });
  old.resolve(); await first;
  assert.equal(ui.slider.disabled, true);
  recent.resolve(); await second;
  assert.deepEqual(rendered, ['recent']);
  assert.equal(ui.slider.disabled, false);
  assert.equal(ui.status.hidden, true);
});

test('errors and retry are localized, and cached slider updates stay enabled', async () => {
  for (const locale of ['en', 'ja']) {
    const ui = panel(locale);
    let fail = true;
    await ui.controller.run(async () => { if (fail) throw Error('offline'); });
    assert.equal(ui.button.hidden, false);
    assert.equal(ui.slider.disabled, true);
    assert.equal(ui.button.textContent, locale === 'ja' ? '再試行' : 'Retry');
    fail = false;
    await ui.button.click();
    assert.equal(ui.slider.disabled, false);
    const pending = deferred();
    const update = ui.controller.run(() => pending.promise, {loading: false});
    assert.equal(ui.slider.disabled, false);
    pending.resolve(); await update;
  }
});

test('a cached rendering failure still shows a retry control', async () => {
  const ui = panel();
  await ui.controller.run(async () => { throw Error('render failed'); }, {loading: false});
  assert.equal(ui.status.hidden, false);
  assert.equal(ui.button.hidden, false);
  assert.equal(ui.slider.disabled, true);
});
