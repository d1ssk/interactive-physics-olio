(() => {
  if (window.location.hostname !== "d1ssk.github.io" || window.self !== window.top) return;
  if (window.__pagesAnalyticsInitialized) return;
  window.__pagesAnalyticsInitialized = true;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () {
    window.dataLayer.push(arguments);
  };
  window.gtag("js", new Date());
  window.gtag("config", "G-P4BVZ9ZZ0E");
  const script = document.createElement("script");
  script.async = true;
  script.src = "https://www.googletagmanager.com/gtag/js?id=G-P4BVZ9ZZ0E";
  document.head.appendChild(script);
})();
