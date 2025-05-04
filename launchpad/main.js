const { app, BrowserWindow } = require('electron');
const path = require('path');

let splash;
function createSplash() {
  splash = new BrowserWindow({
    width: 800,
    height: 450,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    resizable: false,
    webPreferences: {
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });
  splash.loadFile('splash.html');

  // After N ms, destroy splash and open your real window:
  const DURATION = 3000; // or read from a JSON config
  setTimeout(() => {
    // createYourMainWindow();  // <-- hook in your real app here
    splash.close();
  }, DURATION);
}

app.whenReady().then(createSplash);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});