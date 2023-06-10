const { ipcRenderer } = require('electron');
const { PythonShell } = require('python-shell');

let inputFilePath = null;
let outputFilePath = null;
let isEncodeMode = true;

window.addEventListener('DOMContentLoaded', () => {
  const inputButton = document.getElementById('inputButton');
  const outputButton = document.getElementById('outputButton');
  const runButton = document.getElementById('runButton');
  const modeButton = document.getElementById('modeButton');

  inputButton.addEventListener('click', () => {
    ipcRenderer.send('open-file-dialog');
  });

  outputButton.addEventListener('click', () => {
    ipcRenderer.send('save-file-dialog');
  });

  runButton.addEventListener('click', () => {
    let options = {
      mode: 'text',
      pythonPath: 'python', 
      pythonOptions: ['-u'],
      scriptPath: 'py-code',
      args: [inputFilePath, outputFilePath, isEncodeMode],
    };

    PythonShell.run('main.py', options).then((messages) => {
      console.log('results: %j', messages);
    });
  });

  modeButton.addEventListener('click', () => {
    isEncodeMode = !isEncodeMode;
    modeButton.textContent = isEncodeMode ? 'Encode Mode' : 'Decode Mode';
    ipcRenderer.send('set-encode-mode', isEncodeMode);
    console.log(isEncodeMode)
  });

  ipcRenderer.on('selected-input-file', (event, path) => {
    console.log('Selected input file:', path);
    inputFilePath = path;
    checkFilePaths();
  });

  ipcRenderer.on('selected-output-file', (event, path) => {
    console.log('Selected output file:', path);
    outputFilePath = path;
    checkFilePaths();
  });

  function checkFilePaths() {
    if (inputFilePath && outputFilePath) {
      runButton.disabled = false;
    } else {
      runButton.disabled = true;
    }
  }
});
