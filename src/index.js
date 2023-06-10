const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');

if (require('electron-squirrel-startup')) {
  app.quit();
}

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));
  mainWindow.webContents.openDevTools();
};

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

ipcMain.on('open-file-dialog', (event) => {
  dialog.showOpenDialog({
    properties: ['openFile'],
    // filters: [{ name: 'Videos', extensions: ['mp4', 'avi', 'mkv'] }],
  }).then((result) => {
    const filePaths = result.filePaths;
    if (filePaths && filePaths.length > 0) {
      const inputFilePath = filePaths[0];
      event.sender.send('selected-input-file', inputFilePath);
    }
  }).catch((err) => {
    console.log(err);
  });
});

ipcMain.on('save-file-dialog', (event) => {
  dialog.showSaveDialog({
    title: 'Select Output Video Path',
    defaultPath: 'output.mp4',
    filters: [{ name: 'Videos', extensions: ['mp4'] }],
  }).then((result) => {
    const filePath = result.filePath;
    if (filePath) {
      event.sender.send('selected-output-file', filePath);
    }
  }).catch((err) => {
    console.log(err);
  });
});