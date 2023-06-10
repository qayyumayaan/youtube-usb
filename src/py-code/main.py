from encodeAndDecode import Encode, Decode


inputFilePath = r"C:\Users\amazi\Downloads\Youtube data.png"
outputVideoPath = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\videoMade.mp4"
inputVideoPath = outputVideoPath
outputFilePath = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\decoded.png"

Encode(inputFilePath, outputVideoPath)

Decode(inputVideoPath, outputFilePath)