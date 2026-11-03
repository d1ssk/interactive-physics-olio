// Export the authored HTML card through a local Chrome DevTools endpoint.
// Run a repository-root HTTP server and Chrome with --remote-debugging-port first.
import {writeFile} from "node:fs/promises";

const origin = process.argv[2] || "http://127.0.0.1:8000";
const debuggerOrigin = process.argv[3] || "http://127.0.0.1:9222";
const target = await fetch(`${debuggerOrigin}/json/new?about:blank`, {method: "PUT"})
  .then(response => response.json());
const socket = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  socket.addEventListener("open", resolve, {once: true});
  socket.addEventListener("error", reject, {once: true});
});
let nextId = 0;
const pending = new Map();
socket.addEventListener("message", event => {
  const message = JSON.parse(event.data);
  const request = pending.get(message.id);
  if (!request) return;
  pending.delete(message.id);
  if (message.error) request.reject(new Error(JSON.stringify(message.error)));
  else request.resolve(message.result);
});
function command(method, params = {}) {
  const id = ++nextId;
  const result = new Promise((resolve, reject) => pending.set(id, {resolve, reject}));
  socket.send(JSON.stringify({id, method, params}));
  return result;
}
try {
  await command("Page.enable");
  await command("Emulation.setDeviceMetricsOverride", {
    width: 1200, height: 630, deviceScaleFactor: 1, mobile: false,
  });
  const url = `${origin}/scripts/assets/social-card.html`;
  await command("Page.navigate", {url});
  let ready = false;
  for (let attempt = 0; attempt < 100; attempt++) {
    const {result} = await command("Runtime.evaluate", {
      expression: `location.href === ${JSON.stringify(url)} && document.readyState === "complete"
        && document.fonts.status === "loaded" && document.fonts.check('600 68px "Source Serif"')
        && document.images.length === 1 && document.images[0].naturalWidth > 0`,
      returnByValue: true,
    });
    if (result.value) { ready = true; break; }
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  if (!ready) throw new Error("The social card image and font did not finish loading.");
  const decoded = await command("Runtime.evaluate", {
    expression: `(async () => {
      await document.fonts.ready;
      await Promise.all([...document.images].map(image => image.decode()));
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    })()`,
    awaitPromise: true,
  });
  if (decoded.exceptionDetails) throw new Error("The social card image could not be decoded.");
  const {data} = await command("Page.captureScreenshot", {format: "png"});
  await writeFile("docs/assets/images/social-card.png", Buffer.from(data, "base64"));
} finally {
  await command("Page.close");
  socket.close();
}
