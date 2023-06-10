const { PythonShell } = require('python-shell');

let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
};

// let pyshell = new PythonShell('src/py-code/main.py', options);

window.addEventListener('DOMContentLoaded', () => {

//   pyshell.on('message', function (message) {
//     try {
//       const parsedMessage = JSON.parse(message);
//       if (parsedMessage.response !== undefined) {
//         createMessageElement('Bot: ' + parsedMessage.response);
//       }
//     } catch (error) {
//       console.log(message);
//     }
//   });


});