/* Rendering and playback only. Both coordinate systems share precomputed physics. */
(() => {
  const locale = new URLSearchParams(location.search).get('lang') === 'ja' ? 'ja' : 'en';
  const strings = {
    en: {
      title: 'Three wavenumbers: freezing of the field amplitude',
      intro: 'Three fixed comoving wavenumbers evolve at the same cosmic time. Compare their widths on identical axes; use the shared zoom to inspect freezing.',
      play: 'Play', pause: 'Pause', reset: 'Reset', crossing: 'Middle crossing', late: 'Late time', speed: 'Speed',
      time: 'Time (e-folds relative to the middle mode’s Hubble crossing)',
      canonical: 'Use original canonical coordinates \\(Q,P\\)', zoom: 'Shared zoom',
      wide: 'Full view (±24)', medium: 'Intermediate (±6)', close: 'Close view (±4)',
      units: 'Both axes in units of \\(H/(2\\pi)\\)',
      sub: 'Inside the Hubble radius', cross: 'Hubble crossing', super: 'Outside the Hubble radius',
      rescaledNote: 'Dashed green lines: the frozen horizontal width, \\(X=\\pm H/(2\\pi)\\). The bar below each contour shows its horizontal projection (±1 standard deviation). The vertical coordinate is the field velocity divided by the physical wavenumber, with the same spectral weighting as the field.',
      canonicalNote: 'The original canonical coordinates preserve contour area. The horizontal width keeps growing even though the field amplitude freezes. The plot below continues to show the physical field width.',
      history: 'Field width at each wavenumber',
      historyNote: 'Colors match the three panels; colored vertical lines mark their Hubble crossings. All three curves approach the dashed horizontal line at 1, the frozen width in units of \\(H/(2\\pi)\\).',
      contourNote: 'The contour encloses about 39% of the Gaussian Wigner density. Rescaling changes its area, not the quantum state or its purity. Axes remain fixed during playback; zoom is shared by all three panels.',
      panelAlt: 'Gaussian Wigner contour and horizontal width',
      historyAlt: 'Three field widths approach the same frozen amplitude at different times',
      error: 'The animation could not load. Reload the page to try again.',
    },
    ja: {
      title: '三つの波数：場の振幅の凍結',
      intro: '固定した三つの共動波数を、共通の宇宙時刻で追います。同じ目盛りで幅を比べ、共通ズームで凍結付近を拡大してください。',
      play: '再生', pause: '一時停止', reset: '最初に戻る', crossing: '中央の crossing へ', late: '晩期へ', speed: '再生速度',
      time: '時刻（中央のモードの Hubble crossing を基準とする e-fold 数）',
      canonical: '元の正準座標 \\(Q,P\\) で表示', zoom: '共通ズーム',
      wide: '全体（±24）', medium: '中間（±6）', close: '拡大（±4）',
      units: '両軸の単位：\\(H/(2\\pi)\\)',
      sub: 'Hubble 半径の内側', cross: 'Hubble crossing', super: 'Hubble 半径の外側',
      rescaledNote: '緑の破線は凍結後の横幅 \\(X=\\pm H/(2\\pi)\\) の目安です。等高線の下の棒は横方向への射影（±1 標準偏差）を示します。縦座標は場の速度を物理波数で割り、場と同じスペクトルの重みを掛けた量です。',
      canonicalNote: '元の正準座標では等高線の面積が保存されます。場の振幅が凍結しても、横幅は伸び続けます。下のグラフは引き続き元の場の幅を示します。',
      history: '各波数での場の幅',
      historyNote: '色は上の三つのパネルと対応し、色付きの縦線は各波数の Hubble crossing を示します。三つの曲線は \\(H/(2\\pi)\\) 単位での凍結値 1 を示す水平破線に近づきます。',
      contourNote: '等高線が囲むのは Gaussian Wigner 密度の約 39% です。座標の rescaling で面積は変わりますが、量子状態や純粋性は変わりません。再生中の目盛りは固定され、ズームは三つのパネルで共通です。',
      panelAlt: 'Gaussian Wigner 等高線と横方向の幅',
      historyAlt: '三つの波数の場の幅が異なる時刻に同じ凍結値に近づく様子',
      error: 'アニメーションを読み込めませんでした。ページを再読み込みしてください。',
    },
  };
  const t = strings[locale], $ = id => document.getElementById(id);
  document.documentElement.lang = locale;
  document.title = t.title;
  document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t[el.dataset.i18n]; });
  $('history').setAttribute('aria-label', t.historyAlt);
  const ns = 'http://www.w3.org/2000/svg';
  function element(tag, attrs, parent, label) {
    const node = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([name, value]) => node.setAttribute(name, value));
    if (label !== undefined) node.textContent = label;
    parent.append(node);
    return node;
  }
  let data, current = 0, playing = false, handle = null, last = 0, elapsed = 0;
  const frameDuration = 65 / 3;
  const panels = [];
  let historyMarker, historyDots, historyWidth = 900;
  const px = (q, limit) => 207 + 153 * q / limit;
  const py = (p, limit) => 177 - 153 * p / limit;
  const path = (ring, limit) => ring.map(([q,p], i) => `${i ? 'L' : 'M'}${px(q,limit)},${py(p,limit)}`).join(' ') + ' Z';
  function setupPanel(mode, i) {
    const section = document.createElement('section');
    section.className = `mode-card mode-${i}`;
    const ratio = ['k_*/2', 'k_*', '2k_*'][i];
    section.innerHTML = `<h3>\\(k=${ratio}\\)</h3>
      <p class="regime"></p><div class="plot"><svg viewBox="0 0 400 410" role="img"></svg>
      <span class="x-label rescaled-only">\\(X/[H/(2\\pi)]\\)</span><span class="y-label rescaled-only">\\(Y/[H/(2\\pi)]\\)</span>
      <span class="x-label canonical-only" hidden>\\(Q\\)</span><span class="y-label canonical-only" hidden>\\(P\\)</span></div>
      <p class="readouts"><span>\\(x\\): <output class="mode-x"></output></span><span>\\(\\sigma_X/[H/(2\\pi)]\\): <output class="mode-width"></output></span></p>`;
    $('mode-panels').append(section);
    const svg = section.querySelector('svg');
    svg.setAttribute('aria-label', `${t.panelAlt} (${i+1})`);
    const defs = element('defs', {}, svg), clip = element('clipPath', {id:`clip-${i}`}, defs);
    element('rect', {x:54, y:24, width:306, height:306}, clip);
    const grid = element('g', {}, svg);
    const group = element('g', {'clip-path':`url(#clip-${i})`}, svg);
    const reference = element('path', {class:'reference'}, group);
    const ring = element('path', {class:'contour'}, group);
    const width = element('path', {class:'width-guide'}, svg);
    panels.push({section, grid, reference, ring, width});
  }
  const hx = n => 60 + (historyWidth-78) * (n-data.times[0]) / (data.times.at(-1)-data.times[0]);
  const hy = width => 204 - 160 * Math.log10(width / 0.2) / Math.log10(20 / 0.2);
  function setupHistory() {
    const svg = $('history');
    historyWidth = Math.max(320, svg.clientWidth);
    svg.setAttribute('viewBox', `0 0 ${historyWidth} 245`);
    svg.replaceChildren();
    for (const tick of [0.2,0.5,1,2,5,10,20]) {
      element('line', {x1:60, x2:historyWidth-18, y1:hy(tick), y2:hy(tick), class:tick===1?'reference':'grid'}, svg);
      element('text', {x:48, y:hy(tick)+5, 'text-anchor':'end'}, svg, tick);
    }
    for (const tick of [-2,-1,0,1,2]) {
      if(tick<data.times[0] || tick>data.times.at(-1)) continue;
      element('text', {x:hx(tick), y:232, 'text-anchor':'middle'}, svg, tick);
    }
    historyDots = data.modes.map((mode,i) => {
      const group = element('g', {class:`mode-${i}`}, svg);
      element('line', {x1:hx(mode.crossing), x2:hx(mode.crossing), y1:28, y2:210, class:'crossing-marker'}, group);
      const d = mode.rescaledWidths.map((width,j) => `${j?'L':'M'}${hx(data.times[j])},${hy(width[0])}`).join(' ');
      element('path', {d, class:'history-curve'}, group);
      return element('circle', {r:4, class:'history-dot'}, group);
    });
    historyMarker = element('line', {y1:28,y2:210,class:'time-marker'}, svg);
  }
  function updateAxes() {
    const canonical = $('canonical').checked, limit = data.limits[Number($('zoom').value)];
    document.querySelectorAll('.canonical-only').forEach(el => { el.hidden = !canonical; });
    document.querySelectorAll('.rescaled-only').forEach(el => { el.hidden = canonical; });
    for (const panel of panels) {
      panel.grid.replaceChildren();
      for (const tick of [-limit,-limit/2,0,limit/2,limit]) {
        element('line', {x1:px(tick,limit),x2:px(tick,limit),y1:24,y2:330,class:'grid'}, panel.grid);
        element('line', {x1:54,x2:360,y1:py(tick,limit),y2:py(tick,limit),class:'grid'}, panel.grid);
        element('text', {x:px(tick,limit),y:352,'text-anchor':'middle'}, panel.grid,tick);
        element('text', {x:44,y:py(tick,limit)+5,'text-anchor':'end'}, panel.grid,tick);
      }
      panel.reference.setAttribute('d', canonical?'':[-1,1].map(v=>`M${px(v,limit)},24V390`).join(' '));
    }
    render();
    window.dispatchEvent(new Event('physics-atlas:plot-rendered'));
  }
  function render() {
    const canonical = $('canonical').checked, key = canonical?'canonical':'rescaled';
    const limit = data.limits[Number($('zoom').value)], n = data.times[current];
    $('time').value = current;
    $('n').value = n.toFixed(3);
    $('time').setAttribute('aria-valuetext', `N = ${n.toFixed(3)}`);
    panels.forEach((panel,i) => {
      const mode = data.modes[i], transform = mode[key][current], widths = mode[`${key}Widths`][current];
      // Apply the supplied drawing transform; no physical evolution is calculated here.
      const ring = data.circle.map(([u,v])=>transform.map(row=>row[0]*u+row[1]*v));
      panel.ring.setAttribute('d', path(ring,limit));
      const left = px(-Math.min(widths[0],limit),limit), right = px(Math.min(widths[0],limit),limit);
      panel.width.setAttribute('d', `M${left},370H${right}M${left},365V375M${right},365V375`);
      panel.section.querySelector('.mode-x').value = mode.x[current].toFixed(3);
      panel.section.querySelector('.mode-width').value = mode.rescaledWidths[current][0].toFixed(3);
      panel.section.querySelector('.regime').textContent = Math.abs(n-mode.crossing)<1e-9?t.cross:mode.x[current]>1?t.sub:t.super;
      historyDots[i].setAttribute('cx',hx(n)); historyDots[i].setAttribute('cy',hy(mode.rescaledWidths[current][0]));
    });
    historyMarker.setAttribute('x1',hx(n)); historyMarker.setAttribute('x2',hx(n));
  }
  function stop() {
    playing=false; cancelAnimationFrame(handle); handle=null; $('play').textContent=t.play;
  }
  function step(now) {
    handle=null;
    if (!playing) return;
    elapsed+=Math.min(now-last,100)*Number($('speed').value); last=now;
    if (elapsed>=frameDuration) {
      current=Math.min(current+Math.floor(elapsed/frameDuration),data.times.length-1); elapsed%=frameDuration;
      render();
      if(current===data.times.length-1) { stop(); return; }
    }
    handle=requestAnimationFrame(step);
  }
  $('play').addEventListener('click',()=>{
    if(playing) return stop();
    if(current===data.times.length-1) current=0;
    playing=true; elapsed=0; last=performance.now(); $('play').textContent=t.pause;
    render(); handle=requestAnimationFrame(step);
  });
  $('time').addEventListener('input',()=>{stop(); current=Number($('time').value); render();});
  $('reset').addEventListener('click',()=>{stop(); current=0; render();});
  $('crossing').addEventListener('click',()=>{stop(); current=data.times.findIndex(n=>n===0); render();});
  $('late').addEventListener('click',()=>{stop(); current=data.times.length-1; render();});
  $('canonical').addEventListener('change',updateAxes);
  $('zoom').addEventListener('change',updateAxes);
  document.addEventListener('visibilitychange',()=>{if(document.hidden) stop();});
  window.addEventListener('pagehide',stop);
  const historyObserver = new ResizeObserver(() => {
    if(data && Math.abs(Math.max(320,$('history').clientWidth)-historyWidth)>1) {
      setupHistory(); render();
    }
  });
  historyObserver.observe($('history'));
  window.addEventListener('pagehide',()=>historyObserver.disconnect(),{once:true});
  async function typeset() {
    if (!window.MathJax?.startup?.promise) await new Promise(resolve=>window.addEventListener('physics-atlas:mathjax-ready',resolve,{once:true}));
    await MathJax.startup.promise;
    const main = document.querySelector('main');
    MathJax.typesetClear([main]); await MathJax.typesetPromise([main]);
    window.dispatchEvent(new Event('physics-atlas:mathjax-ready'));
  }
  fetch('freezing.json').then(response=>{if(!response.ok) throw Error('data'); return response.json();}).then(async payload=>{
    data=payload;
    data.modes.forEach(setupPanel); setupHistory();
    $('time').max=data.times.length-1;
    updateAxes(); await typeset();
    ['play','reset','crossing','late','time','canonical','zoom'].forEach(id=>$(id).disabled=false);
  }).catch(()=>{$('error').hidden=false; $('error').textContent=t.error;});
})();
