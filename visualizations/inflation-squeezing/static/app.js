/* Rendering only: every frame's physical coordinates come from physics.py. */
(() => {
  const locale = new URLSearchParams(location.search).get('lang') === 'ja' ? 'ja' : 'en';
  const strings = {
    en: {
      title: 'One standing mode: rotation + squeeze',
      rotationTitle: 'Rotation', squeezeTitle: 'Squeeze', totalTitle: 'Total · Bunch–Davies state',
      intro: 'Follow one fixed comoving wavenumber. Pause or drag the time slider to choose a time.',
      play: 'Play', pause: 'Pause', reset: 'Reset', crossing: 'Hubble crossing', speed: 'Speed',
      time: 'Time (e-folds relative to Hubble crossing)', directions: 'Directions on the total flow',
      none: 'None', flow: 'Instantaneous flow', principal: 'Ellipse principal axes', solutions: 'Growing / decaying solutions',
      noneNote: 'The contour and orange markers evolve with the full time-dependent Hamiltonian.',
      flowNote: 'Dashed orange: instantaneous stretching; dotted green: instantaneous contraction. Shown only for \\(x<1\\). These are not solution trajectories.',
      principalNote: 'Dashed orange: broad principal axis; dotted green: narrow principal axis. These covariance axes are orthogonal.',
      solutionsNote: 'Dashed orange: exact solution growing at late times; dotted green: exact solution decaying at late times. They are generally not orthogonal and are not the ellipse axes.',
      axes: 'At every time: horizontal \\(Q=\\sqrt{k}a\\phi\\), vertical \\(P=a\\phi^\\prime/\\sqrt{k}\\), with \\(\\phi=\\phi_{A,\\mathbf k}\\). The axes neither rotate nor rescale.',
      arrows: 'Arrow vectors share the display factor \\(1/\\sqrt{1+x^2}\\) and a fixed drawing scale.',
      sub: 'Inside the Hubble radius · instantaneous elliptic flow', cross: 'Hubble crossing · instantaneous shear (nonzero flow)', super: 'Outside the Hubble radius · instantaneous hyperbolic flow',
      acoustic: 'Toy acoustic power: coherent versus random temporal phase',
      acousticNote: 'Equal total initial variance in both ensembles. A fixed temporal phase preserves oscillations in power; independent cosine and sine amplitudes wash them out. This is not a CMB spectrum calculation.',
      rotationAlt: 'Clockwise rotation field in fixed Q and P quadratures', squeezeAlt: 'Stretching in Q and contraction in P', totalAlt: 'Total Hamiltonian flow and the evolving Gaussian Wigner contour', acousticAlt: 'Normalized coherent power oscillates between zero and one; incoherent power is one half',
      error: 'The animation could not load. Reload the page to try again.',
    },
    ja: {
      title: '一つの定在波モード：回転＋スクイーズ',
      rotationTitle: '回転', squeezeTitle: 'スクイーズ', totalTitle: '合成流・Bunch–Davies 状態',
      intro: '固定した一つの共動波数を追います。一時停止やスライダーで時刻を選べます。',
      play: '再生', pause: '一時停止', reset: '最初に戻る', crossing: 'Hubble crossingへ', speed: '再生速度',
      time: '時刻（Hubble crossingを基準とするe-fold数）', directions: '合成流に重ねる方向',
      none: '表示しない', flow: '瞬間的な流れの固有方向', principal: '楕円の主軸', solutions: '厳密な成長解・減衰解の方向',
      noneNote: '楕円とオレンジの点は、時間依存Hamiltonian全体による流れに従います。',
      flowNote: 'オレンジの破線：瞬間的な伸長方向。緑の点線：瞬間的な収縮方向。\\(x<1\\) でのみ表示します。これらは解の軌道ではありません。',
      principalNote: 'オレンジの破線：楕円の長軸。緑の点線：短軸。共分散行列で決まる二つの主軸は直交します。',
      solutionsNote: 'オレンジの破線：晩期に成長する厳密解。緑の点線：晩期に減衰する厳密解。一般に直交せず、楕円の主軸とも異なります。',
      axes: 'どの時刻でも、横軸は\\(Q=\\sqrt{k}a\\phi\\)、縦軸は\\(P=a\\phi^\\prime/\\sqrt{k}\\)、ただし\\(\\phi=\\phi_{A,\\mathbf k}\\)です。軸は回転せず、縮尺も変わりません。',
      arrows: '矢印には共通の表示係数\\(1/\\sqrt{1+x^2}\\)と固定の描画縮尺を掛けています。',
      sub: 'Hubble半径の内側・瞬間的な流れは楕円型', cross: 'Hubble crossing・瞬間的な流れはシアー（流れは止まりません）', super: 'Hubble半径の外側・瞬間的な流れは双曲型',
      acoustic: '音響振動の模型：時間位相が揃う場合とランダムな場合のパワー',
      acousticNote: '両集団の初期振幅の分散の総和を揃えています。時間位相が一定ならパワーの振動が残り、cos成分とsin成分が独立なら消えます。CMBスペクトルそのものの計算ではありません。',
      rotationAlt: '固定したQ、P座標での時計回りの回転場', squeezeAlt: 'Q方向の伸長とP方向の収縮', totalAlt: '合成Hamilton流とGaussian Wigner等高線の時間発展', acousticAlt: 'コヒーレントなパワーは0と1の間で振動し、非コヒーレントなパワーは2分の1で一定',
      error: 'アニメーションを読み込めませんでした。ページを再読み込みしてください。',
    },
  };
  const t = strings[locale];
  const $ = id => document.getElementById(id);
  document.documentElement.lang = locale;
  document.title = t.title;
  document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t[el.dataset.i18n]; });
  ['rotation', 'squeeze', 'total'].forEach(id => $(id).setAttribute('aria-label', t[`${id}Alt`]));
  $('direction-note').textContent = t.noneNote;
  // Localization runs before deferred initial typesetting; support late script loading too.
  if (window.MathJax?.startup?.promise) {
    MathJax.startup.promise.then(async () => {
      MathJax.typesetClear([document.querySelector('main')]);
      await MathJax.typesetPromise([document.querySelector('main')]);
      window.dispatchEvent(new Event('physics-atlas:mathjax-ready'));
    });
  }
  const ns = 'http://www.w3.org/2000/svg';
  function element(tag, attrs = {}, parent) {
    const el = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));
    if (parent) parent.append(el);
    return el;
  }
  function text(parent, x, y, label, attrs = {}) {
    const el = element('text', {x, y, ...attrs}, parent); el.textContent = label;
  }
  let data, current = 0, playing = false, last = 0, elapsed = 0, animationHandle = null;
  const panels = [];
  const px = q => 214 + q / data.limit * 158;
  const py = p => 190 - p / data.limit * 158;
  function polyline(points, close = false) {
    return points.map(([q, p], i) => `${i ? 'L' : 'M'}${px(q).toFixed(2)},${py(p).toFixed(2)}`).join(' ') + (close ? ' Z' : '');
  }
  function setupPanel(id) {
    const svg = $(id);
    const defs = element('defs', {}, svg), clip = element('clipPath', {id: `clip-${id}`}, defs);
    element('rect', {x:56, y:32, width:316, height:316}, clip);
    for (const tick of [-4, -2, 0, 2, 4]) {
      element('line', {x1:px(tick), x2:px(tick), y1:32, y2:348, class:'grid'}, svg);
      element('line', {x1:56, x2:372, y1:py(tick), y2:py(tick), class:'grid'}, svg);
      text(svg, px(tick), 370, tick, {'text-anchor':'middle'});
      text(svg, 46, py(tick)+5, tick, {'text-anchor':'end'});
    }
    const group = element('g', {'clip-path':`url(#clip-${id})`}, svg);
    const field = element('path', {class:'flow-arrows'}, group);
    const overlay = [0,1].map(i => element('path', {class:`direction-${i}`, fill:'none'}, group));
    const ring = element('path', {class:'contour'}, group);
    const markers = Array.from({length:12}, () => element('circle', {r:3.5, class:'marker'}, group));
    return {field, overlay, ring, markers};
  }
  function arrowPath(vectors) {
    return vectors.map(([u,v], i) => {
      const [q,p] = data.points[i], x = px(q), y = py(p);
      const dx = u * 7.2, dy = -v * 7.2, len = Math.hypot(dx,dy);
      if (len < .01) return '';
      const tipX=x+dx, tipY=y+dy, head=Math.min(5,len*.38), ux=dx/len, uy=dy/len;
      return `M${x},${y}L${tipX},${tipY}M${tipX-head*ux-head*.5*uy},${tipY-head*uy+head*.5*ux}L${tipX},${tipY}L${tipX-head*ux+head*.5*uy},${tipY-head*uy-head*.5*ux}`;
    }).join(' ');
  }
  function render() {
    const f = data.frames[current];
    $('time').value = current;
    for (const key of ['x','n','r']) $(key).value = f[key].toFixed(3);
    $('angle').value = `${f.angle.toFixed(2)}°`;
    $('time').setAttribute('aria-valuetext', `N = ${f.n.toFixed(3)}, x = ${f.x.toFixed(3)}`);
    $('regime').textContent = Math.abs(f.n)<1e-10 ? t.cross : f.x>1 ? t.sub : t.super;
    panels.forEach((panel, i) => {
      panel.field.setAttribute('d', arrowPath(f.fields[i]));
      panel.ring.setAttribute('d', i===2 ? polyline(f.ring,true) : '');
      panel.markers.forEach((marker,j) => {
        marker.style.display = i===2 ? '' : 'none';
        marker.setAttribute('cx',px(f.markers[j][0])); marker.setAttribute('cy',py(f.markers[j][1]));
      });
      const directions = i===2 ? (f[$('directions').value] || []) : [];
      panel.overlay.forEach((line,j) => line.setAttribute('d', directions[j] ? polyline([directions[j].map(v=>-v),directions[j]]) : ''));
    });
  }
  function stop() {
    playing=false; cancelAnimationFrame(animationHandle); animationHandle=null;
    $('play').textContent=t.play;
  }
  function step(now) {
    animationHandle=null;
    if (!playing) return;
    elapsed += Math.min(now-last,100) * Number($('speed').value); last=now;
    if (elapsed>=65) {
      current = Math.min(current+Math.floor(elapsed/65),data.frames.length-1); elapsed%=65; render();
      if (current===data.frames.length-1) { stop(); return; }
    }
    animationHandle=requestAnimationFrame(step);
  }
  $('play').addEventListener('click', () => {
    if (playing) return stop();
    if (current===data.frames.length-1) current=0;
    playing=true; elapsed=0; last=performance.now(); $('play').textContent=t.pause; render(); animationHandle=requestAnimationFrame(step);
  });
  $('time').addEventListener('input', () => { stop(); current=Number($('time').value); render(); });
  $('reset').addEventListener('click', () => { stop(); current=0; render(); });
  $('crossing').addEventListener('click', () => { stop(); current=data.frames.findIndex(f=>Math.abs(f.n)<1e-10); render(); });
  let directionMath=Promise.resolve();
  $('directions').addEventListener('change', () => {
    if(data) render();
    directionMath=directionMath.then(async()=>{
      if(!window.MathJax?.startup?.promise) await new Promise(resolve=>window.addEventListener('physics-atlas:mathjax-ready',resolve,{once:true}));
      await MathJax.startup.promise;
      const note=$('direction-note');
      MathJax.typesetClear([note]); note.textContent=t[`${$('directions').value}Note`];
      await MathJax.typesetPromise([note]);
      window.dispatchEvent(new Event('physics-atlas:mathjax-ready'));
    });
  });
  document.addEventListener('visibilitychange', () => { if(document.hidden) stop(); });
  window.addEventListener('pagehide',stop);
  fetch('data.json').then(response => {if(!response.ok) throw Error('data'); return response.json();}).then(payload => {
    data=payload; ['rotation','squeeze','total'].forEach(id=>panels.push(setupPanel(id)));
    $('time').max=data.frames.length-1;
    ['play','reset','crossing','time'].forEach(id=>$(id).disabled=false);
    render();
  }).catch(() => { $('error').hidden=false; $('error').textContent=t.error; });
})();
