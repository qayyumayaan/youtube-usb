from encodeAndDecode import Encode, Decode
import sys

inputFilePath = sys.argv[1]
outputVideoPath = sys.argv[2]
encode = sys.argv[3]

color_mapping = {
    'D': (50, 50, 50),  # black
    'W': (255, 255, 255), # white
    'R': (0, 0, 255),   # red
    'G': (0, 255, 0),   # green
    'B': (255, 0, 0),   # blue
    'C': (255, 255, 0), # cyan
    'P': (128, 0, 128), # purple
    'Y': (0, 255, 255), # yellow
}

frameRate = 30.0
resHorizontal = 1920
resVertical = 1080
dataPointSideLengthRes = 120
colorThreshold = 20

if encode.lower() == "true":
    print("Encoding mode!")
    Encode(inputFilePath, outputVideoPath, color_mapping, frameRate, resHorizontal, resVertical, dataPointSideLengthRes)
else:
    print("Decoding mode!")
    inputVideoPath = inputFilePath
    outputFilePath = outputVideoPath
    Decode(inputVideoPath, outputFilePath, color_mapping, resHorizontal, resVertical, dataPointSideLengthRes, colorThreshold)