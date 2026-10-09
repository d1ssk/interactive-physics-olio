(() => {
    if (window.parent === window) return;
    const PARENT_TARGET_ORIGIN = window.location.origin;
    function report() {
      const main = document.querySelector("main");
      const contentBottom = main ? main.getBoundingClientRect().bottom : 0;
      const contentHeight = Math.max(contentBottom, document.body.getBoundingClientRect().height);
      const frameHeight = Math.ceil(contentHeight);
      if (window.frameElement) {
        window.frameElement.style.minHeight = "0";
        window.frameElement.style.height = `${frameHeight}px`;
        window.frameElement.setAttribute("scrolling", "no");
        window.frameElement.style.overflow = "hidden";
      }
      window.parent.postMessage(
        {type: "physics-atlas:frame-height", height: frameHeight},
        PARENT_TARGET_ORIGIN,
      );
    }
    window.addEventListener("load", report);
    window.addEventListener("resize", report);
    window.addEventListener("physics-atlas:mathjax-ready", report);
    window.addEventListener("physics-atlas:plot-rendered", report);
    window.addEventListener("message", event => {
      const expectedParent = event.source === window.parent;
      const expectedOrigin = event.origin === PARENT_TARGET_ORIGIN;
      if (expectedParent && expectedOrigin && event.data?.type === "physics-atlas:request-frame-height") {
        report();
      }
    });
    if ("ResizeObserver" in window) {
      const observer = new ResizeObserver(report);
      observer.observe(document.body);
      const main = document.querySelector("main");
      if (main) observer.observe(main);
      window.addEventListener("pagehide", () => observer.disconnect(), {once:true});
    }
    document.fonts?.ready.then(report);
    report();
  })();
