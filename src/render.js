const { ipcRenderer } = require('electron');
const { PythonShell } = require('python-shell');

let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
};

let pyshell = new PythonShell('src/py-code/main.py', options);

window.addEventListener('DOMContentLoaded', () => {
  const inputButton = document.getElementById('inputButton');
  const outputButton = document.getElementById('outputButton');

  inputButton.addEventListener('click', () => {
    ipcRenderer.send('open-file-dialog');
  });

  outputButton.addEventListener('click', () => {
    ipcRenderer.send('save-file-dialog');
  });

  ipcRenderer.on('selected-input-file', (event, path) => {
    console.log('Selected input file:', path);
    pyshell.send(path);
  });

  ipcRenderer.on('selected-output-file', (event, path) => {
    console.log('Selected output file:', path);
    pyshell.send(path);
  });

  // Handle messages received from main.py
  pyshell.on('message', function (message) {
    console.log(message)
  });
});