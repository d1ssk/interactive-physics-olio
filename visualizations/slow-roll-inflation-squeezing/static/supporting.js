/* Plotly views of precomputed slow-roll data; the browser evaluates no physical formula. */
(() => {
  const {locale, t: shared, typeset, load, selectors} = window.SlowRollUI;
  const view = window.slowRollView;
  const strings = {
    en: {
      backgroundTitle: 'The slow-roll background and its parameters',
      backgroundIntro: 'Each potential is integrated from the slow-roll attractor until the end of inflation, defined by \\(\\epsilon_1=1\\). Time runs to the right; the horizontal axis counts e-folds relative to the end.',
      potentialHeading: 'Potential and the field at five exit times',
      flowHeading: 'Hubble-flow parameters',
      backgroundNote: String.raw`Left: \(V(\phi)\) divided by its value when the pivot exits 55 e-folds before the end, with the field marked at \(N_{\mathrm{end}}-N=55,25,10,5,0\) (\(\phi\) in units of \(M_{\mathrm{Pl}}\)). Right: solid curves are the exact \(\epsilon_1=-\dot H/H^2\) and \(\epsilon_2=d\ln\epsilon_1/dN\) of the numerical background; dashed curves are the potential estimates \(\epsilon_V\) and \(4\epsilon_V-2\eta_V\). They agree while both are small and separate in the last few e-folds.`,
      frequenciesTitle: 'Gradient term against the background term',
      frequenciesIntro: 'The same three wavenumbers as the main animation, from deep inside the Hubble radius to the end of inflation (or twelve e-folds later for power-law inflation).',
      pumpHeading: 'Second-order form: k² against z″/z',
      rateHeading: 'Phase-space form: rotation x against squeeze σ',
      frequencyNote: String.raw`Left: \(x_j^2=k_j^2/\mathcal H^2\) against \(z''/(z\mathcal H^2)\) (black) and \(a''/(a\mathcal H^2)=2-\epsilon_1\) (gold, dashed), on a logarithmic axis. Right: the coefficients of the generator \(A=xJ+\sigma D\): the rotation rate \(x_j\) against the squeeze rate \(\sigma=1+\epsilon_2/2\) (black) and the tensor value \(\sigma_T=1\) (gold, dashed). The flow becomes hyperbolic when \(x_j<\sigma\). The background terms stay near 2 and 1 during slow roll and change only in the last few e-folds.`,
      modesTitle: 'The pivot mode: numerical solution and two approximations',
      modesIntro: 'Follow the middle wavenumber from \\(x=20\\) to the end of inflation. The horizontal axis is e-folds relative to its Hubble crossing.',
      display: 'Display', canonical: 'Canonical variable', curvature: 'Curvature perturbation', ratio: 'Ratio to approximations', squeezing: 'Squeezing magnitude',
      canonicalHeading: String.raw`Canonical mode \(\sqrt2\,|F|=\sqrt{2k}\,|f_k|\)`,
      curvatureHeading: String.raw`Curvature mode \(\zeta_k\), normalized to its final magnitude`,
      ratioHeading: String.raw`Ratios \(|F|/|F_{\mathrm{dS}}|\) and \(|F|/|F_{\nu}|\)`,
      squeezingHeading: String.raw`Squeezing magnitude \(r_k\)`,
      canonicalNote: String.raw`Logarithmic axis. Solid: numerical solution. Dotted: Hankel approximation based on the background at Hubble crossing. Dashed: de Sitter at the same \(x\). Compare their agreement near crossing and their later drift. The reference is defined in §8.`,
      curvatureNote: String.raw`Real part (blue), imaginary part (orange), and magnitude (green) of \(\zeta_k\propto xHF/\sqrt{\epsilon_1}\), divided by its final magnitude. The global phase is chosen so that the conserved part is imaginary, as in the companion article. Dashed: the magnitude of the de Sitter test field \(\phi_k\propto xF_{\mathrm{dS}}\), normalized in the same way. After crossing, \(\zeta_k\) stays constant to the end of inflation.`,
      ratioNote: String.raw`Ratio of the numerical canonical magnitude to the two references. Both start close to 1. The de Sitter ratio drifts after crossing because \(|F|\propto z\) grows faster than \(1/x\); the Hankel ratio stays near 1 while \(\epsilon_1\) and \(\epsilon_2\) remain close to their crossing values and departs as their evolution accumulates. Even for the Starobinsky pivot 55 e-folds before the end, the final Hankel ratio reaches about 51.3.`,
      squeezingNote: String.raw`Solid: numerical \(r_k\). Dotted: constant-\(\nu\) Hankel. Dashed: de Sitter \(\operatorname{arsinh}(1/2x)\). Late-time slopes approach \(\sigma=1+\epsilon_2/2\) per e-fold, so \(r_k\) tracks \(\ln z\) up to a constant.`,
      spectrumTitle: 'Primordial spectra at the end of inflation',
      spectrumIntro: 'Scalar and tensor powers from about forty numerically evolved wavenumbers, normalized so the scalar power is 2.1 × 10⁻⁹ at the pivot. For the ending models the pivot exits 55 e-folds before the end.',
      powerHeading: 'Scalar and tensor power spectra', powerErrorHeading: 'Relative error near pivot', powerErrorFull: 'Relative error: full range',
      powerAria: 'Power spectrum display',
      cmbNote: String.raw`The shaded band marks approximate primary-CMB scales: \(10^{-4}\lesssim k\lesssim0.2\,\mathrm{Mpc}^{-1}\), identifying the pivot with \(k_*=0.05\,\mathrm{Mpc}^{-1}\). This corresponds roughly to \(\ell\simeq2\text{–}3000\).`,
      spectrumErrorNote: String.raw`Left: signed residual \(\mathcal P_{\mathrm{num}}/\mathcal P_{\mathrm{approx}}-1\) for scalars (blue) and tensors (orange), using the leading formula (dashed) or the next-order formula (dotted). Zero means agreement; positive values mean the approximation underestimates the power. Choose the near-pivot view to resolve the correction, or the full range to follow the departure near the end. Right: the selected quantity. The last two e-folds also include modes that have not frozen, so their residuals are not solely slow-roll truncation errors.`,
      tiltNs: 'Scalar spectral index', tiltR: 'Tensor-to-scalar ratio', tiltNt: 'Tensor tilt and consistency', tiltEnd: 'Squeezing at the end',
      tiltAria: 'Quantity shown in the second plot',
      spectrumNote: String.raw`Left: \(\mathcal P_\zeta\) (blue) and \(\mathcal P_T\) (orange) from the numerical modes, evaluated at the end of inflation (power law: twelve or more e-folds after crossing), against the leading slow-roll formula at \(k=aH\) (dashed) and its next-order correction (dotted). Right: the selected quantity against its first-order slow-roll value (dashed). Modes that exit in the last two e-folds are not yet frozen at the end.`,
      plotAlt: 'Interactive scientific plot; pan to move and use the wheel to zoom. The caption defines its axes.',
    },
    ja: {
      backgroundTitle: 'slow-roll 背景とパラメータ',
      backgroundIntro: '各ポテンシャルについて、slow-roll のアトラクターから \\(\\epsilon_1=1\\) で定義するインフレーション終了まで背景を積分しています。時間は右向きに進み、横軸は終了時刻からの e-fold 数です。',
      potentialHeading: 'ポテンシャルと五つの時刻での場の値',
      flowHeading: 'Hubble flow パラメータ',
      backgroundNote: String.raw`左：pivot が終了の 55 e-fold 前に出るときの値で割った \(V(\phi)\) と、\(N_{\mathrm{end}}-N=55,25,10,5,0\) での場の値（\(\phi\) は \(M_{\mathrm{Pl}}\) 単位）。右：実線は数値解の背景から求めた厳密な \(\epsilon_1=-\dot H/H^2\) と \(\epsilon_2=d\ln\epsilon_1/dN\)、破線はポテンシャルから見積もった \(\epsilon_V\) と \(4\epsilon_V-2\eta_V\) です。両者は小さい間は一致し、最後の数 e-fold で離れます。`,
      frequenciesTitle: '勾配項と背景項の競合',
      frequenciesIntro: 'メインのアニメーションと同じ三つの波数を、Hubble 半径の十分内側からインフレーションの終了まで（べき乗則では 12 e-fold 後まで）示します。',
      pumpHeading: '二階の方程式：k² と z″/z',
      rateHeading: '位相空間の流れ：回転 x とスクイーズ σ',
      frequencyNote: String.raw`左：\(x_j^2=k_j^2/\mathcal H^2\) と \(z''/(z\mathcal H^2)\)（黒）、\(a''/(a\mathcal H^2)=2-\epsilon_1\)（金の破線）の対数表示。右：生成子 \(A=xJ+\sigma D\) の係数、すなわち回転の速さ \(x_j\) とスクイーズの速さ \(\sigma=1+\epsilon_2/2\)（黒）、テンソルの値 \(\sigma_T=1\)（金の破線）。\(x_j<\sigma\) で流れは双曲型になります。背景項は slow-roll の間はほぼ 2 と 1 に留まり、最後の数 e-fold でだけ大きく変わります。`,
      modesTitle: 'pivot モード：数値解と二つの近似',
      modesIntro: '中央の波数を \\(x=20\\) からインフレーションの終了まで追います。横軸はこのモードの Hubble crossing からの e-fold 数です。',
      display: '表示', canonical: '正準変数', curvature: '曲率摂動', ratio: '近似解との比', squeezing: 'squeezing の大きさ',
      canonicalHeading: String.raw`正準変数のモード \(\sqrt2\,|F|=\sqrt{2k}\,|f_k|\)`,
      curvatureHeading: String.raw`曲率摂動のモード \(\zeta_k\)（最終的な大きさで規格化）`,
      ratioHeading: String.raw`比 \(|F|/|F_{\mathrm{dS}}|\) と \(|F|/|F_{\nu}|\)`,
      squeezingHeading: String.raw`squeezing の大きさ \(r_k\)`,
      canonicalNote: String.raw`縦軸は対数表示です。実線は数値解、点線は Hubble crossing 時の背景を基準にした Hankel 近似、破線は同じ \(x\) での de Sitter の解です。crossing 付近での一致と、その後のずれを比べてください。近似の詳しい定義は §8 にまとめています。`,
      curvatureNote: String.raw`\(\zeta_k\propto xHF/\sqrt{\epsilon_1}\) の実部（青）、虚部（オレンジ）、絶対値（緑）を最終的な絶対値で割ったものです。前編と同じく、保存成分が虚部になるよう全体の位相を選んでいます。破線は de Sitter テスト場 \(\phi_k\propto xF_{\mathrm{dS}}\) の絶対値を同様に規格化したものです。crossing 後の \(\zeta_k\) はインフレーションの終了まで一定です。`,
      ratioNote: String.raw`数値解の正準変数の絶対値と二つの参照解の比です。どちらも 1 付近から始まります。de Sitter との比は crossing 後にずれていきます。\(|F|\propto z\) が \(1/x\) より速く増えるからです。Hankel 解との比は、\(\epsilon_1,\epsilon_2\) が crossing での値に近い間は 1 付近に留まり、変化の蓄積とともに離れます。Starobinsky 模型の終了 55 e-fold 前の pivot でも、終了時の Hankel 解との比は約 51.3 になります。`,
      squeezingNote: String.raw`実線は数値解の \(r_k\)、点線は定数 \(\nu\) の Hankel 解、破線は de Sitter の \(\operatorname{arsinh}(1/2x)\) です。晩期の傾きは 1 e-fold あたり \(\sigma=1+\epsilon_2/2\) に近づくので、\(r_k\) は定数を除いて \(\ln z\) に沿って増えます。`,
      spectrumTitle: 'インフレーション終了時の原始スペクトル',
      spectrumIntro: '約 40 個の波数を数値的に時間発展させて求めたスカラーとテンソルのパワーです。pivot でのスカラーのパワーが 2.1 × 10⁻⁹ になるよう規格化しています。終了するモデルでは、pivot は終了の 55 e-fold 前に Hubble 半径を出ます。',
      powerHeading: 'スカラーとテンソルのパワースペクトル', powerErrorHeading: '相対誤差（pivot 付近）', powerErrorFull: '相対誤差（全範囲）',
      powerAria: 'パワースペクトルの表示',
      cmbNote: String.raw`薄い帯は CMB の一次異方性で見るスケールの目安です。pivot を \(k_*=0.05\,\mathrm{Mpc}^{-1}\) に対応づけ、\(10^{-4}\lesssim k\lesssim0.2\,\mathrm{Mpc}^{-1}\) を示しています。多重極ではおおよそ \(\ell\simeq2\text{–}3000\) に対応します。`,
      spectrumErrorNote: String.raw`左：スカラー（青）とテンソル（オレンジ）の符号付き相対誤差 \(\mathcal P_{\mathrm{num}}/\mathcal P_{\mathrm{approx}}-1\)。最低次の式を破線、次の次数の補正を点線で示します。零は一致、正の値は近似の過小評価を表します。pivot 付近の表示で補正の効果を、全範囲の表示で終了付近のずれを確認できます。右：選んだ量。最後の 2 e-fold にはまだ凍結していないモードも含まれるため、その差は slow-roll 展開の打切り誤差だけではありません。`,
      tiltNs: 'スカラーのスペクトル指数', tiltR: 'テンソル・スカラー比', tiltNt: 'テンソルの傾きと無矛盾性関係', tiltEnd: '終了時の squeezing',
      tiltAria: '右の図に表示する量',
      spectrumNote: String.raw`左：数値解から求めた \(\mathcal P_\zeta\)（青）と \(\mathcal P_T\)（オレンジ）をインフレーション終了時（べき乗則では crossing から 12 e-fold 以上後）に評価し、\(k=aH\) で評価した slow-roll の最低次の式（破線）と次の次数の補正（点線）と比べています。右：選んだ量と、その一次の slow-roll 近似（破線）。最後の 2 e-fold で出るモードは、終了時にはまだ凍結していません。`,
      plotAlt: 'インタラクティブな科学図。ドラッグで移動、ホイールで拡大できます。軸の定義は説明文に記載しています。',
    },
  };
  const t = {...shared, ...strings[locale]};
  const $ = id => document.getElementById(id);
  document.documentElement.lang = locale;
  document.title = t[`${view}Title`];
  $('figure-title').textContent = t[`${view}Title`];
  $('figure-intro').textContent = t[`${view}Intro`];
  document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t[el.dataset.i18n]; });
  document.querySelectorAll('.chart').forEach(el => el.setAttribute('aria-label', t.plotAlt));
  $('tilt-choice').setAttribute('aria-label', t.tiltAria);
  $('power-choice').setAttribute('aria-label', t.powerAria);

  const blue = '#397da9', orange = '#d26541', green = '#569d88', gold = '#a37d2b', ink = '#28333d', grid = '#ded6cc';
  const modeColors = [blue, orange, green];
  const config = {responsive: true, displaylogo: false, scrollZoom: true, modeBarButtonsToRemove: ['lasso2d', 'select2d']};
  const plots = [];
  function layout(xTitle, yTitle, extra = {}) {
    const {xaxis = {}, yaxis = {}, ...rest} = extra;
    return {
      margin: {l: 58, r: 15, t: 34, b: 52}, font: {family: 'system-ui, sans-serif', size: 11, color: ink},
      paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)', dragmode: 'pan',
      xaxis: {title: {text: xTitle, standoff: 8}, gridcolor: grid, zeroline: false, ...xaxis},
      yaxis: {title: {text: yTitle, standoff: 6}, gridcolor: grid, zeroline: false, ...yaxis},
      legend: {orientation: 'h', y: 1.02, yanchor: 'bottom', x: 0, font: {size: 10}}, ...rest,
    };
  }
  function line(x, y, name, color, dash = 'solid', width = 2) {
    return {type: 'scatter', mode: 'lines', x, y, name, line: {color, dash, width}, hovertemplate: '%{x:.3f}, %{y:.5g}<extra>%{fullData.name}</extra>'};
  }
  function vertical(x, color = ink, dash = 'dot') {
    return {type: 'line', xref: 'x', yref: 'paper', x0: x, x1: x, y0: 0, y1: 1, line: {color, dash, width: 1}};
  }
  async function plot(id, traces, spec) {
    await Plotly.react($(id), traces, spec, config);
    if (!plots.includes(id)) plots.push(id);
    window.dispatchEvent(new Event('physics-atlas:plot-rendered'));
  }
  async function note(id, value) {
    const target = $(id);
    target.textContent = value;
    await typeset([target]);
  }

  async function background(d) {
    const markText = d.marks.beforeEnd.map(n => `N_end − N = ${n}`);
    await plot('potential-plot', [
      line(d.phi, d.potential, 'V(φ)/V*', ink),
      {type: 'scatter', mode: 'markers+text', x: d.marks.phi, y: d.marks.potential, name: 'Exit times', text: d.marks.beforeEnd.map(String),
        textposition: 'top center', marker: {color: orange, size: 9}, hovertext: markText, hovertemplate: '%{hovertext}<br>φ = %{x:.3f}, V/V* = %{y:.4g}<extra></extra>'},
    ], layout('Inflaton field φ / M_Pl', 'V / V*', {
      showlegend: false, yaxis: {range: [0, 1.5], autorange: false},
    }));
    await plot('flow-plot', [
      line(d.n, d.eps1, 'ε1 (exact)', blue), line(d.n, d.eps2, 'ε2 (exact)', orange),
      line(d.n, d.epsV, 'ε_V', blue, 'dash', 1.5), line(d.n, d.eps2V, '4ε_V − 2η_V', orange, 'dash', 1.5),
    ], layout('N − N_end', 'Parameter value', {
      xaxis: {range: [-70, 0], autorange: false},
      // Logarithmic ranges use base-10 exponents; include every model's exact and estimated values.
      yaxis: {type: 'log', range: [-4, 2], autorange: false}, shapes: [vertical(-55)],
    }));
  }

  async function frequencies(d) {
    const h = d.history;
    const end = h.n[h.n.length - 1];
    const range = [-3.2, end];
    const square = values => values.map(x => x * x);
    await plot('pump-plot', [
      ...h.x.map((x, j) => line(h.n, square(x), `x${j + 1}²`, modeColors[j])),
      line(h.n, h.pump, 'z″/(z𝓗²)', ink, 'solid', 2.5), line(h.n, h.tensorPump, 'a″/(a𝓗²)', gold, 'dash'),
    ], layout('N − N_cross,*', 'Term divided by 𝓗²', {xaxis: {range}, yaxis: {type: 'log', range: [-3, 3.5]}, shapes: [vertical(0)]}));
    await plot('rate-plot', [
      ...h.x.map((x, j) => line(h.n, x, `x${j + 1}`, modeColors[j])),
      line(h.n, h.sigma, 'σ = 1 + ε2/2', ink, 'solid', 2.5), line(h.n, h.n.map(() => 1), 'σ_T = 1', gold, 'dash'),
    ], layout('N − N_cross,*', 'Rate per e-fold', {xaxis: {range}, yaxis: {type: 'log', range: [-2, 2]}, shapes: [vertical(0)]}));
  }

  async function modes(d) {
    const h = d.history, choice = $('mode-choice').value;
    let traces, spec;
    if (choice === 'canonical') {
      traces = [line(h.n, h.canonical[2], 'Numerical', blue, 'solid', 2.5), line(h.n, h.canonicalHankel[2], 'Constant-ν Hankel', ink, 'dot'),
        line(h.n, h.canonicalDeSitter[2], 'de Sitter test field', orange, 'dash')];
      spec = layout('N − N_cross,* (e-folds from Hubble crossing)', '√2 |F|', {yaxis: {type: 'log'}, shapes: [vertical(0)]});
    } else if (choice === 'curvature') {
      traces = [line(h.n, h.curvature[0], 'Re ζ', blue), line(h.n, h.curvature[1], 'Im ζ', orange), line(h.n, h.curvature[2], '|ζ|', green, 'solid', 2.5),
        line(h.n, h.fieldDeSitter[2], '|φ| de Sitter', ink, 'dash', 1.5)];
      spec = layout('N − N_cross,* (e-folds from Hubble crossing)', 'Normalized mode', {xaxis: {range: [-3, Math.min(h.n[h.n.length - 1], 8)]}, shapes: [vertical(0)]});
    } else if (choice === 'ratio') {
      const ratio = reference => h.canonical[2].map((v, i) => v / reference[2][i]);
      traces = [line(h.n, ratio(h.canonicalDeSitter), '|F| / |F_dS|', orange, 'dash'), line(h.n, ratio(h.canonicalHankel), '|F| / |F_ν|', ink, 'dot', 2.5)];
      spec = layout('N − N_cross,* (e-folds from Hubble crossing)', 'Ratio', {shapes: [vertical(0)]});
    } else {
      traces = [line(h.n, h.r, 'Numerical', blue, 'solid', 2.5), line(h.n, h.rHankel, 'Constant-ν Hankel', ink, 'dot'), line(h.n, h.rDeSitter, 'de Sitter', orange, 'dash')];
      spec = layout('N − N_cross,* (e-folds from Hubble crossing)', 'r_k', {shapes: [vertical(0)]});
    }
    await plot('mode-plot', traces, spec);
    await note('mode-heading', t[`${choice}Heading`]);
    await note('mode-note', t[`${choice}Note`]);
  }

  const format = value => {
    const [mantissa, exponent] = value.toExponential(2).split('e');
    const superscript = String(Number(exponent)).replace(/[-0-9]/g, c => '⁻⁰¹²³⁴⁵⁶⁷⁸⁹'[c === '-' ? 0 : Number(c) + 1]);
    return `${mantissa} × 10${superscript}`;
  };
  async function spectrum(d) {
    const p = d.pivot, ending = d.beforeEnd !== null;
    const [cmbLow, cmbHigh] = d.cmbWindow.lnk;
    const cmbGuide = {
      shapes: [{
        type: 'rect', xref: 'x', yref: 'paper', x0: cmbLow, x1: cmbHigh, y0: 0, y1: 1,
        fillcolor: 'rgba(101, 122, 135, 0.12)', line: {width: 0}, layer: 'below',
      }, vertical(0)],
      annotations: [{
        x: (cmbLow + cmbHigh) / 2, y: 0.98, xref: 'x', yref: 'paper',
        text: 'CMB', showarrow: false, yanchor: 'top', font: {size: 10, color: '#58616a'},
      }],
    };
    $('ns').value = p.ns.toFixed(4); $('ratio').value = p.r.toPrecision(3);
    $('nt').value = p.nt.toPrecision(3); $('consistency').value = (-p.r / 8).toPrecision(3);
    $('hubble').value = format(p.hubbleGeV); $('energy').value = format(p.energyGeV);
    $('squeezing-end').value = p.squeezing.toFixed(1);
    document.querySelectorAll('.ending-only').forEach(el => { el.hidden = !ending; });
    const endOption = $('tilt-choice').querySelector('option[value="end"]');
    endOption.disabled = !ending;
    if (!ending && $('tilt-choice').value === 'end') $('tilt-choice').value = 'ns';
    const hover = ending ? d.beforeEnd.map(n => `N_end − N at crossing = ${n}`) : d.lnk.map(() => '');
    const withHover = trace => ({...trace, text: hover, hovertemplate: '%{x:.3f}, %{y:.5g}<br>%{text}<extra>%{fullData.name}</extra>'});
    const powerChoice = $('power-choice').value;
    const relative = powerChoice !== 'power';
    if (relative) {
      const nearPivot = powerChoice === 'relative';
      const values = Object.values(d.relativeErrors).flatMap(series => series.filter((_, i) => Math.abs(d.lnk[i]) <= 10));
      const low = Math.min(0, ...values), high = Math.max(0, ...values);
      const pad = Math.max((high - low) * 0.15, 1e-5);
      const residual = (name, label, color, dash) => withHover(line(d.lnk, d.relativeErrors[name], label, color, dash));
      await plot('power-plot', [
        residual('scalarLeading', 'Scalar / leading − 1', blue, 'dash'),
        residual('scalarNext', 'Scalar / next order − 1', blue, 'dot'),
        residual('tensorLeading', 'Tensor / leading − 1', orange, 'dash'),
        residual('tensorNext', 'Tensor / next order − 1', orange, 'dot'),
      ], layout('ln(k / k_*)', 'P_numerical / P_approximation − 1', {
        xaxis: nearPivot ? {range: [-10, 10]} : {},
        yaxis: {zeroline: true, zerolinecolor: ink, ...(nearPivot ? {range: [low - pad, high + pad]} : {})},
        ...cmbGuide, margin: {l: 64, r: 15, t: 70, b: 52},
      }));
    } else {
      await plot('power-plot', [
        withHover({...line(d.lnk, d.scalar, 'P_ζ numerical', blue, 'solid', 2.5), mode: 'lines+markers', marker: {size: 5}}),
        line(d.lnk, d.scalarLeading, 'P_ζ leading', blue, 'dash', 1.5), line(d.lnk, d.scalarNext, 'P_ζ next order', blue, 'dot', 1.5),
        withHover({...line(d.lnk, d.tensor, 'P_T numerical', orange, 'solid', 2.5), mode: 'lines+markers', marker: {size: 5}}),
        line(d.lnk, d.tensorLeading, 'P_T leading', orange, 'dash', 1.5), line(d.lnk, d.tensorNext, 'P_T next order', orange, 'dot', 1.5),
      ], layout('ln(k / k_*)', 'Dimensionless power', {yaxis: {type: 'log', exponentformat: 'power'}, ...cmbGuide, margin: {l: 64, r: 15, t: 70, b: 52}}));
    }
    // For ending models, open on the range of modes that exit at least five e-folds before the end.
    const focus = (...series) => {
      if (!ending) return {};
      const values = series.flatMap(s => s.filter((_, i) => d.beforeEnd[i] >= 5));
      const low = Math.min(...values), high = Math.max(...values), pad = 0.15 * (high - low) + 1e-3;
      return {range: [low - pad, high + pad]};
    };
    const choice = $('tilt-choice').value;
    let traces, yTitle, yaxis = {};
    if (choice === 'ns') {
      traces = [withHover(line(d.lnk, d.ns, 'n_s numerical', blue, 'solid', 2.5)), line(d.lnk, d.nsFirst, '1 − 2ε1 − ε2', ink, 'dash')];
      yTitle = 'n_s'; yaxis = focus(d.ns, d.nsFirst);
    } else if (choice === 'r') {
      traces = [withHover(line(d.lnk, d.r, 'r numerical', blue, 'solid', 2.5)), line(d.lnk, d.rFirst, '16ε1', ink, 'dash')];
      yTitle = 'r'; yaxis = {type: 'log', exponentformat: 'power'};
    } else if (choice === 'nt') {
      traces = [withHover(line(d.lnk, d.nt, 'n_T numerical', orange, 'solid', 2.5)), line(d.lnk, d.consistency, '−r/8 numerical', blue, 'dash'),
        line(d.lnk, d.ntFirst, '−2ε1', ink, 'dot')];
      yTitle = 'Tensor tilt'; yaxis = focus(d.nt, d.consistency, d.ntFirst);
    } else {
      traces = [withHover({...line(d.lnk, d.squeezingEnd, 'r_k at the end', blue, 'solid', 2.5), mode: 'lines+markers', marker: {size: 5}})];
      yTitle = 'Squeezing magnitude r_k';
    }
    await plot('tilt-plot', traces, layout('ln(k / k_*)', yTitle, {yaxis, ...cmbGuide, margin: {l: 64, r: 15, t: 70, b: 52}}));
    await note('spectrum-note', relative ? t.spectrumErrorNote : t.spectrumNote);
  }

  const renderers = {background, frequencies, modes, spectrum};
  let request = 0, currentKey = null, renderQueue = Promise.resolve();
  async function show(key) {
    const token = ++request;
    currentKey = key;
    try {
      const prefix = view === 'background' || view === 'spectrum' ? view : 'config';
      const [data] = await Promise.all([load(`${prefix}-${key}`), window.plotReady]);
      if (token !== request) return;
      // Serialize Plotly/MathJax work too: an older render must finish before a newer one.
      renderQueue = renderQueue.catch(() => {}).then(async () => {
        if (token !== request) return;
        await renderers[view](data);
        if (token === request) $('support-error').hidden = true;
      });
      await renderQueue;
    } catch (error) {
      if (token === request) fail();
    }
  }
  function fail() {
    $('support-error').hidden = false;
    $('support-error').textContent = t.error;
  }
  const options = {
    background: {endingOnly: true, withExit: false},
    frequencies: {},
    modes: {},
    spectrum: {withExit: false},
  }[view];
  const parameterHost = view === 'background' ? null : $('parameter-choice');
  if (!parameterHost) $('parameter-choice').hidden = true;
  const key = selectors($('model-choice'), parameterHost, options, next => show(next).catch(fail));
  $('mode-choice').addEventListener('change', () => show(currentKey).catch(fail));
  $('tilt-choice').addEventListener('change', () => show(currentKey).catch(fail));
  $('power-choice').addEventListener('change', () => show(currentKey).catch(fail));
  let resizeTimer, lastWidth = window.innerWidth;
  window.addEventListener('resize', () => {
    if (window.innerWidth === lastWidth) return;
    lastWidth = window.innerWidth;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      Promise.all(plots.filter(id => $(id).getClientRects().length).map(id => Plotly.Plots.resize($(id)))).catch(fail);
    }, 100);
  });
  typeset([document.querySelector('main')])
    .then(() => show(key()))
    .then(() => {
      document.documentElement.dataset.ready = 'true';
      window.dispatchEvent(new Event('physics-atlas:plot-rendered'));
    })
    .catch(fail);
})();
