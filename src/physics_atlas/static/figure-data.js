/* Lossless figure-chunk loading. Plotly receives copies, never the cached source. */
(() => {
  function unpack(document) {
    if (document.format !== 1 || !Array.isArray(document.pool)) throw new Error("Invalid figure data");
    const expand = (value, ancestors = new Set()) => {
      if (Array.isArray(value)) return value.map(item => expand(item, ancestors));
      if (value && typeof value === "object") {
        if (Object.hasOwn(value, "$ref")) {
          const index = value.$ref;
          if (!Number.isInteger(index) || index < 0 || index >= document.pool.length || ancestors.has(index)) {
            throw new Error("Invalid figure reference");
          }
          return expand(document.pool[index], new Set([...ancestors, index]));
        }
        return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, expand(item, ancestors)]));
      }
      return value;
    };
    return expand(document.root);
  }

  function createStore(manifest, base, fetcher = globalThis.fetch.bind(globalThis)) {
    const cache = new Map();
    const ready = new Set();
    return {
      has(key) { return ready.has(key); },
      load(key) {
        if (!Object.hasOwn(manifest.chunks, key)) return Promise.reject(new Error("Unknown figure chunk"));
        if (!cache.has(key)) {
          const promise = Promise.resolve().then(async () => {
            const response = await fetcher(new URL(manifest.chunks[key], base));
            if (!response.ok) throw new Error(`Figure request failed: ${response.status}`);
            const data = unpack(await response.json());
            ready.add(key);
            return data;
          }).catch(error => { cache.delete(key); throw error; });
          cache.set(key, promise);
        }
        return cache.get(key);
      },
    };
  }

  // A newer selection owns the UI even if an older request finishes last.
  function createPanel(element, sliders, locale) {
    const messages = locale === "ja"
      ? {loading: "図を読み込んでいます…", error: "選択した図を読み込めませんでした。再試行してください。", retry: "再試行"}
      : {loading: "Loading figure…", error: "Could not load the selected figure. Please retry.", retry: "Retry"};
    const status = element.querySelector("[data-figure-status]");
    const text = status.querySelector("[role=status]");
    const retry = status.querySelector("button");
    retry.textContent = messages.retry;
    let revision = 0;
    let action;
    const run = async (task, {loading = true} = {}) => {
      action = task;
      const ticket = ++revision;
      const current = () => ticket === revision;
      element.setAttribute("aria-busy", "true");
      element.setAttribute("data-figure-state", loading ? "loading" : "ready");
      sliders.forEach(slider => { slider.disabled = loading; });
      status.hidden = !loading;
      text.textContent = messages.loading;
      retry.hidden = true;
      try {
        await task(current);
        if (!current()) return;
        element.setAttribute("data-figure-state", "ready");
        status.hidden = true;
        text.textContent = "";
        sliders.forEach(slider => { slider.disabled = false; });
      } catch (error) {
        if (!current()) return;
        element.setAttribute("data-figure-state", "error");
        status.hidden = false;
        sliders.forEach(slider => { slider.disabled = true; });
        text.textContent = messages.error;
        retry.hidden = false;
      } finally {
        if (current()) element.setAttribute("aria-busy", "false");
      }
    };
    retry.addEventListener("click", () => run(action));
    return {run};
  }
  globalThis.PhysicsFigureData = {unpack, createStore, createPanel};
})();
