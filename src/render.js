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
  let magicNumberInput = document.getElementById('magicNumber');

  magicNumberInput.addEventListener('input', checkFilePaths);

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
      args: [inputFilePath, outputFilePath, isEncodeMode, magicNumberInput.value],
    };

    PythonShell.run('main.py', options).then((messages) => {
      console.log('results: %j', messages);
    });
  });

  modeButton.addEventListener('click', () => {
    isEncodeMode = !isEncodeMode;
    modeButton.textContent = isEncodeMode ? 'Encode Mode' : 'Decode Mode';
    ipcRenderer.send('set-encode-mode', isEncodeMode);
    console.log(isEncodeMode);
  
    if (!isEncodeMode) {
      magicNumberInput.style.display = 'none';
    } else {
      magicNumberInput.style.display = 'block';
    }
  
    checkFilePaths();
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
    const magicNumberInput = document.getElementById('magicNumber');
    const runButton = document.getElementById('runButton');
  
    if (isEncodeMode) {
      if (inputFilePath && outputFilePath) {
        runButton.disabled = false;
      } else {
        runButton.disabled = true;
      }
      magicNumberInput.style.display = 'none';
    } else {
      if (inputFilePath && outputFilePath && magicNumberInput.value !== '') {
        runButton.disabled = false;
      } else {
        runButton.disabled = true;
      }
      magicNumberInput.style.display = 'block';
    }
  }
  
});
