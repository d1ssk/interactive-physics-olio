/* Shared UI helpers: locale, model selectors, MathJax queue, and cached data loading.
   No physics is evaluated here; every plotted number comes from the precomputed JSON. */
(() => {
  const locale = new URLSearchParams(location.search).get('lang') === 'ja' ? 'ja' : 'en';
  const strings = {
    en: {
      model: 'Potential', exit: String.raw`Pivot \(k_*\) exits \(N_*\) e-folds before the end`,
      exitAria: "Number of e-folds before the end of inflation when the pivot mode exits",
      constantEps: String.raw`Constant \(\epsilon_1\)`, constantEpsAria: "Constant first slow-roll parameter",
      starobinsky: 'Starobinsky', powerlaw: 'Power law',
      play: 'Play', pause: 'Pause', reset: 'Reset', speed: 'Speed',
      loading: 'Loading…',
      error: 'This figure could not load. Reload the page to try again.',
    },
    ja: {
      model: 'ポテンシャル', exit: String.raw`pivot \(k_*\) が終了の \(N_*\) e-fold 前に Hubble 半径を出る`,
      exitAria: "pivot モードが Hubble 半径を出る時刻（インフレーション終了前の e-fold 数）",
      constantEps: String.raw`一定の \(\epsilon_1\)`, constantEpsAria: "一定の第1 slow-roll パラメータ",
      starobinsky: 'Starobinsky', powerlaw: 'べき乗則',
      play: '再生', pause: '一時停止', reset: '最初に戻る', speed: '再生速度',
      loading: '読み込み中…',
      error: '図を読み込めませんでした。ページを再読み込みしてください。',
    },
  };
  const t = strings[locale];
  const models = [
    {key: 'starobinsky', label: t.starobinsky, ends: true},
    {key: 'phi23', label: String.raw`\(\phi^{2/3}\)`, ends: true},
    {key: 'phi2', label: String.raw`\(\phi^{2}\)`, ends: true},
    {key: 'phi4', label: String.raw`\(\phi^{4}\)`, ends: true},
    {key: 'powerlaw', label: t.powerlaw, ends: false},
  ];
  const exits = ['55', '25', '10', '5'];
  const powerLaw = [['005', '0.05'], ['015', '0.15'], ['030', '0.30']];

  let mathQueue = Promise.resolve();
  function typeset(targets) {
    mathQueue = mathQueue.then(async () => {
      if (!window.MathJax?.startup?.promise) {
        await new Promise(resolve => window.addEventListener('physics-atlas:mathjax-ready', resolve, {once: true}));
      }
      await MathJax.startup.promise;
      MathJax.typesetClear(targets);
      await MathJax.typesetPromise(targets);
      window.dispatchEvent(new Event('physics-atlas:mathjax-ready'));
    });
    return mathQueue;
  }

  const cache = new Map();
  function load(name) {
    if (!cache.has(name)) {
      cache.set(name, fetch(`data/${name}.json`).then(response => {
        if (!response.ok) throw Error(name);
        return response.json();
      }));
    }
    return cache.get(name);
  }

  function segmented(container, labelText, ariaText, options, current, onSelect) {
    container.replaceChildren();
    const label = document.createElement('span');
    label.className = 'choice-label';
    label.textContent = labelText;
    const group = document.createElement('div');
    group.className = 'segmented';
    group.setAttribute('role', 'group');
    group.setAttribute('aria-label', ariaText);
    for (const [value, text] of options) {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = text;
      button.dataset.value = value;
      button.setAttribute('aria-pressed', String(value === current));
      button.addEventListener('click', () => {
        if (button.getAttribute('aria-pressed') === 'true') return;
        group.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
        onSelect(value);
      });
      group.append(button);
    }
    container.append(label, group);
  }

  /* Model and exit-time (or constant-epsilon) selectors; calls onChange(selection). */
  function selectors(modelHost, parameterHost, options, onChange) {
    const allowed = models.filter(model => !options.endingOnly || model.ends);
    const state = {model: allowed[0].key, exit: '55', power: '005'};
    function key() {
      if (state.model === 'powerlaw') return `powerlaw${state.power}`;
      return options.withExit === false ? state.model : `${state.model}-${state.exit}`;
    }
    function drawParameter() {
      if (!parameterHost) return;
      if (state.model === 'powerlaw') {
        segmented(parameterHost, t.constantEps, t.constantEpsAria, powerLaw, state.power, value => { state.power = value; onChange(key()); });
      } else if (options.withExit !== false) {
        segmented(parameterHost, t.exit, t.exitAria, exits.map(n => [n, n]), state.exit, value => { state.exit = value; onChange(key()); });
      } else {
        parameterHost.replaceChildren();
      }
      parameterHost.hidden = !parameterHost.childElementCount;
      typeset([parameterHost]);
    }
    segmented(modelHost, t.model, t.model, allowed.map(model => [model.key, model.label]), state.model, value => {
      state.model = value;
      drawParameter();
      onChange(key());
    });
    drawParameter();
    typeset([modelHost]);
    return key;
  }

  window.SlowRollUI = {locale, t, typeset, load, selectors};
})();
