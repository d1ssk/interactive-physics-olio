/* Rendering only: every matrix, squeezing value, and background term comes from physics.py. */
(() => {
  const {locale, t: shared, typeset, load, selectors} = window.SlowRollUI;
  const strings = {
    en: {
      title: 'Three wavenumbers squeezing in turn',
      intro: 'Three comoving wavenumbers cross the Hubble radius 1.5 e-folds apart. Each panel shows the Bunch–Davies state of one standing mode on the same fixed quadratures. Choose a potential and the exit time, then play or drag the time slider.',
      compare: String.raw`Overlay the de Sitter test field at the same \(x\)`,
      time: 'Time (equal steps in e-folds; the middle mode crosses at 0)',
      first: 'crosses first', pivot: 'pivot', last: 'crosses last',
      pumpTitle: 'Gradient term versus background term (logarithmic)',
      rTitle: 'Squeezing magnitude',
      dsLegend: 'de Sitter test field',
      axes: String.raw`Panels: horizontal \(Q=\sqrt{k}\,v_{A,\mathbf k}\), vertical \(P=\pi_{A,\mathbf k}/\sqrt{k}\), identical fixed ranges \(-4.4\) to \(4.4\). Filled: the slow-roll curvature mode, a contour containing 39% of the Wigner probability, with eight material points. Dashed: the de Sitter test field of the companion article at the same \(x=k/(aH)\). Long ellipses leave the frame; their width keeps shrinking.`,
      stripNote: String.raw`Upper strip: each \(x_j^2=k_j^2/\mathcal H^2\) falls below the background term \(z''/(z\mathcal H^2)\simeq2\) near \(x_j\simeq\sqrt2\), shortly before the mode's Hubble crossing at \(x_j=1\); the dashed curve is the tensor and test-field term \(a''/(a\mathcal H^2)=2-\epsilon_1\). Lower strip: solid curves are the slow-roll modes, dashed ones the de Sitter test field evaluated at the same \(x_j\). The vertical line is the current time.`,
      sub: 'All three modes are inside the Hubble radius',
      some: count => `${count} of 3 modes are outside the Hubble radius`,
      all: 'All three modes are outside the Hubble radius',
      panelAlt: index => `Wigner contour of mode ${index + 1} in fixed Q and P quadratures`,
      timeValue: value => `${value} e-folds from pivot Hubble crossing`,
      pumpAlt: 'Squared x of the three modes compared with the background terms, on a logarithmic scale',
      rAlt: 'Squeezing magnitude of the three modes and of the de Sitter test field',
    },
    ja: {
      title: '三つの波数が順に squeezing される',
      intro: '三つの共動波数が 1.5 e-fold ずつずれて Hubble 半径を出ます。各パネルは、一つの定在波モードの Bunch–Davies 状態を、共通の固定した quadrature の上に描いたものです。ポテンシャルと pivot の時刻を選び、再生するか時刻スライダーを動かしてください。',
      compare: String.raw`同じ \(x\) での de Sitter テスト場を重ねる`,
      time: '時刻（e-fold 数で等間隔。中央のモードの Hubble crossing が 0）',
      first: '最初に出る', pivot: 'pivot', last: '最後に出る',
      pumpTitle: '勾配項と背景項（対数表示）',
      rTitle: 'squeezing の大きさ',
      dsLegend: 'de Sitter テスト場',
      axes: String.raw`パネルの横軸は \(Q=\sqrt{k}\,v_{A,\mathbf k}\)、縦軸は \(P=\pi_{A,\mathbf k}/\sqrt{k}\) で、範囲はすべて \(-4.4\) から \(4.4\) に固定しています。塗りつぶしは slow-roll 背景での曲率摂動のモードで、Wigner 確率の 39% を囲む等高線と、流れに乗って動く 8 個の点です。破線は前編の de Sitter テスト場を同じ \(x=k/(aH)\) で描いたものです。細長くなった楕円は枠からはみ出しますが、その幅は縮み続けます。`,
      stripNote: String.raw`上段：各モードの \(x_j^2=k_j^2/\mathcal H^2\) は、\(x_j\simeq\sqrt2\) 付近、つまり \(x_j=1\) の Hubble crossing の少し前に背景項 \(z''/(z\mathcal H^2)\simeq2\) を下回ります。破線はテンソルとテスト場の背景項 \(a''/(a\mathcal H^2)=2-\epsilon_1\) です。下段：実線が slow-roll 背景のモード、破線が同じ \(x_j\) での de Sitter テスト場です。縦線は現在の時刻を示します。`,
      sub: '三つのモードはすべて Hubble 半径の内側にあります',
      some: count => `三つのうち ${count} つのモードが Hubble 半径の外側にあります`,
      all: '三つのモードはすべて Hubble 半径の外側にあります',
      panelAlt: index => `モード ${index + 1} の Wigner 等高線（固定した Q、P 座標）`,
      timeValue: value => `pivot の Hubble crossing から ${value} e-fold`,
      pumpAlt: '三つのモードの x の二乗と背景項の比較（対数表示）',
      rAlt: '三つのモードと de Sitter テスト場の squeezing の大きさ',
    },
  };
  const t = {...shared, ...strings[locale]};
  const $ = id => document.getElementById(id);
  document.documentElement.lang = locale;
  document.title = t.title;
  document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t[el.dataset.i18n]; });
  [0, 1, 2].forEach(i => $(`panel-${i}`).setAttribute('aria-label', t.panelAlt(i)));
  $('pump-strip').setAttribute('aria-label', t.pumpAlt);
  $('r-strip').setAttribute('aria-label', t.rAlt);
  typeset([document.querySelector('main')]);

  const ns = 'http://www.w3.org/2000/svg';
  function element(tag, attrs = {}, parent) {
    const el = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));
    if (parent) parent.append(el);
    return el;
  }
  function text(parent, x, y, label, attrs = {}) {
    const el = element('text', {x, y, ...attrs}, parent);
    el.textContent = label;
  }
  const circle = Array.from({length: 121}, (_, i) => [Math.cos(i * Math.PI / 60), Math.sin(i * Math.PI / 60)]);
  const materialAngles = Array.from({length: 8}, (_, i) => i * Math.PI / 4);
  let data = null, current = 0, playing = false, last = 0, elapsed = 0, handle = null;
  const panels = [];
  const limit = 4.4;
  const px = q => 214 + q / limit * 158;
  const py = p => 190 - p / limit * 158;
  // M (cos, sin)/sqrt(2) is the unit-Mahalanobis contour of Sigma = M M^T/2.
  function mapped(m, points) {
    return points.map(([c, s]) => [(m[0] * c + m[1] * s) / Math.SQRT2, (m[2] * c + m[3] * s) / Math.SQRT2]);
  }
  function path(points, close) {
    return points.map(([q, p], i) => `${i ? 'L' : 'M'}${px(q).toFixed(2)},${py(p).toFixed(2)}`).join('') + (close ? 'Z' : '');
  }
  function setupPanel(i) {
    const svg = $(`panel-${i}`);
    const clip = element('clipPath', {id: `clip-${i}`}, element('defs', {}, svg));
    element('rect', {x: 56, y: 32, width: 316, height: 316}, clip);
    for (const tick of [-4, -2, 0, 2, 4]) {
      element('line', {x1: px(tick), x2: px(tick), y1: 32, y2: 348, class: tick ? 'grid' : 'grid axis'}, svg);
      element('line', {x1: 56, x2: 372, y1: py(tick), y2: py(tick), class: tick ? 'grid' : 'grid axis'}, svg);
      text(svg, px(tick), 370, tick, {'text-anchor': 'middle'});
      text(svg, 46, py(tick) + 5, tick, {'text-anchor': 'end'});
    }
    const group = element('g', {'clip-path': `url(#clip-${i})`}, svg);
    const ring = element('path', {class: `contour mode-${i}`}, group);
    const reference = element('path', {class: `reference mode-${i}`}, group);
    const markers = materialAngles.map(() => element('circle', {r: 3.5, class: `marker mode-${i}`}, group));
    return {ring, reference, markers};
  }

  const strip = {left: 56, right: 788, top: 8, bottom: 172};
  let stripScale = null;
  function sx(n) {
    const w = data.window.n;
    return strip.left + (n - w[0]) / (w[w.length - 1] - w[0]) * (strip.right - strip.left);
  }
  function polyline(svg, xs, ys, cls) {
    const d = xs.map((x, i) => (Number.isFinite(ys[i]) ? `${i && Number.isFinite(ys[i - 1]) ? 'L' : 'M'}${x.toFixed(1)},${ys[i].toFixed(1)}` : '')).join('');
    element('path', {d, class: cls}, svg);
  }
  function drawStrips() {
    const w = data.window, xs = w.n.map(sx);
    const logY = v => strip.bottom - (Math.log10(v) + 3) / 6 * (strip.bottom - strip.top);
    // Values outside the axis are drawn beyond it and removed by the clip path.
    const clampLog = v => logY(Math.min(Math.max(v, 1e-6), 1e6));
    const rMax = Math.max(4, Math.ceil(Math.max(...w.modes.flatMap(m => [...m.r, ...m.rDeSitter]))));
    const linY = v => strip.bottom - v / rMax * (strip.bottom - strip.top);
    stripScale = {logY, linY};
    for (const [id, ticks, y, label] of [
      ['pump-strip', [-3, -2, -1, 0, 1, 2, 3], v => logY(10 ** v), v => (v === 0 ? '1' : `1e${v}`)],
      ['r-strip', Array.from({length: rMax + 1}, (_, i) => i), linY, v => String(v)],
    ]) {
      const svg = $(id);
      svg.replaceChildren();
      const clip = element('clipPath', {id: `${id}-clip`}, element('defs', {}, svg));
      element('rect', {x: strip.left, y: strip.top, width: strip.right - strip.left, height: strip.bottom - strip.top}, clip);
      for (const v of ticks) {
        element('line', {x1: strip.left, x2: strip.right, y1: y(v), y2: y(v), class: 'grid'}, svg);
        text(svg, strip.left - 6, y(v) + 4, label(v), {'text-anchor': 'end', class: 'tick'});
      }
      for (let n = Math.ceil(w.n[0]); n <= w.n[w.n.length - 1]; n++) {
        element('line', {x1: sx(n), x2: sx(n), y1: strip.top, y2: strip.bottom, class: n ? 'grid' : 'grid axis'}, svg);
        text(svg, sx(n), strip.bottom + 18, n, {'text-anchor': 'middle', class: 'tick'});
      }
      const g = element('g', {'clip-path': `url(#${id}-clip)`}, svg);
      if (id === 'pump-strip') {
        w.modes.forEach((m, j) => polyline(g, xs, m.x.map(x => clampLog(x * x)), `series mode-${j}`));
        polyline(g, xs, w.pump.map(clampLog), 'series pump');
        polyline(g, xs, w.tensorPump.map(clampLog), 'series tensor dashed');
      } else {
        w.modes.forEach((m, j) => {
          polyline(g, xs, m.rDeSitter.map(linY), `series mode-${j} dashed ds-line`);
          polyline(g, xs, m.r.map(linY), `series mode-${j}`);
        });
      }
      element('line', {class: 'cursor', y1: strip.top, y2: strip.bottom}, svg);
      if (id === 'r-strip') w.modes.forEach((_, j) => element('circle', {r: 4, class: `dot mode-${j}`}, svg));
    }
  }

  function render() {
    const w = data.window, i = current;
    $('time').value = i;
    $('n').value = w.n[i].toFixed(2);
    $('time').setAttribute('aria-valuetext', t.timeValue(w.n[i].toFixed(2)));
    const compare = $('compare').checked;
    const outside = w.modes.filter(m => m.x[i] < 1).length;
    $('status').textContent = outside === 0 ? t.sub : outside === 3 ? t.all : t.some(outside);
    w.modes.forEach((m, j) => {
      const panel = panels[j];
      const matrix = m.matrix[i];
      panel.ring.setAttribute('d', path(mapped(matrix, circle), true));
      panel.reference.setAttribute('d', compare ? path(mapped(m.matrixDeSitter[i], circle), true) : '');
      mapped(matrix, materialAngles.map(a => [Math.cos(a), Math.sin(a)])).forEach(([q, p], k) => {
        panel.markers[k].setAttribute('cx', px(q).toFixed(2));
        panel.markers[k].setAttribute('cy', py(p).toFixed(2));
      });
      $(`x${j}`).value = m.x[i] < 0.01 ? m.x[i].toExponential(1) : m.x[i].toPrecision(3);
      $(`r${j}`).value = m.r[i].toFixed(3);
      $(`d${j}`).value = m.rDeSitter[i].toFixed(3);
    });
    document.querySelectorAll('.ds').forEach(el => { el.hidden = !compare; });
    document.querySelectorAll('.ds-line').forEach(el => { el.style.display = compare ? '' : 'none'; });
    const x = sx(w.n[i]);
    document.querySelectorAll('.cursor').forEach(line => { line.setAttribute('x1', x); line.setAttribute('x2', x); });
    document.querySelectorAll('#r-strip .dot').forEach((dot, j) => {
      dot.setAttribute('cx', x);
      dot.setAttribute('cy', stripScale.linY(w.modes[j].r[i]));
    });
  }
  function showPivot() {
    const p = data.pivot;
    $('eps1').value = p.eps1.toPrecision(3);
    $('eps2').value = p.eps2.toPrecision(3);
    $('sigma').value = p.sigma.toFixed(4);
    $('nu').value = p.nu.toFixed(4);
  }
  function stop() {
    playing = false;
    cancelAnimationFrame(handle);
    handle = null;
    $('play').textContent = t.play;
  }
  function step(now) {
    handle = null;
    if (!playing) return;
    elapsed += Math.min(now - last, 100) * Number($('speed').value);
    last = now;
    if (elapsed >= 60) {
      current = Math.min(current + Math.floor(elapsed / 60), data.window.n.length - 1);
      elapsed %= 60;
      render();
      if (current === data.window.n.length - 1) { stop(); return; }
    }
    handle = requestAnimationFrame(step);
  }
  $('play').addEventListener('click', () => {
    if (playing) return stop();
    if (current === data.window.n.length - 1) current = 0;
    playing = true; elapsed = 0; last = performance.now();
    $('play').textContent = t.pause;
    render();
    handle = requestAnimationFrame(step);
  });
  $('time').addEventListener('input', () => { stop(); current = Number($('time').value); render(); });
  $('reset').addEventListener('click', () => { stop(); current = 0; render(); });
  $('compare').addEventListener('change', () => { if (data) render(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
  window.addEventListener('pagehide', stop);

  let request = 0;
  async function show(key) {
    const token = ++request;
    const payload = await load(`config-${key}`);
    if (token !== request) return;
    const fraction = data ? current / (data.window.n.length - 1) : 0;
    data = payload;
    current = Math.round(fraction * (data.window.n.length - 1));
    $('time').max = data.window.n.length - 1;
    showPivot();
    drawStrips();
    render();
  }
  function fail() {
    stop();
    $('error').hidden = false;
    $('error').textContent = t.error;
  }
  [0, 1, 2].forEach(i => panels.push(setupPanel(i)));
  const key = selectors($('model-choice'), $('parameter-choice'), {}, next => show(next).catch(fail));
  show(key()).then(() => {
    ['play', 'reset', 'time'].forEach(id => { $(id).disabled = false; });
  }).catch(fail);
})();
