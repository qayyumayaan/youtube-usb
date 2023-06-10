const { ipcRenderer } = require('electron');
const { PythonShell } = require('python-shell');

let inputFilePath = null;
let outputFilePath = null;

window.addEventListener('DOMContentLoaded', () => {
  const inputButton = document.getElementById('inputButton');
  const outputButton = document.getElementById('outputButton');
  const runButton = document.getElementById('runButton');

  inputButton.addEventListener('click', () => {
    ipcRenderer.send('open-file-dialog');
  });

  outputButton.addEventListener('click', () => {
    ipcRenderer.send('save-file-dialog');
  });

  runButton.addEventListener('click', () => {
    let options = {
      mode: 'text',
      pythonOptions: ['-u'], 
      scriptPath: 'src/py-code',
      args: [inputFilePath, outputFilePath] 
    };

    PythonShell.run('main.py', options).then((messages) => {
      console.log('results: %j', messages);
    });
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