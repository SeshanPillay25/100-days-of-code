const { app, BrowserWindow } = require("electron");
const path = require("path");

app.on("ready", function() {
  let window = new BrowserWindow({ width: 800, height: 600 });
  window.loadURL(path.join("file://", __dirname, "static/index.html"));
});
app.on("close", function() {
  window = null;
});
