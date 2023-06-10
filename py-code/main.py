from encodeAndDecode import Encode, Decode
import sys

inputFilePath = sys.argv[1]
outputVideoPath = sys.argv[2]
encode = sys.argv[3]

m = 255
color_mapping = {
    # 'D': (m/2, m/2, m/2),  # black
    'D': (0, 0, 0),  # black
    'R': (0, 0, m),   # red
    'G': (0, m, 0),   # green
    'Y': (0, m, m), # yellow
    'B': (m, 0, 0),   # blue
    'P': (m, 0, m), # purple
    'C': (m, m, 0), # cyan
    'W': (m, m, m), # white
}

frameRate = 30.0
resHorizontal = 1920
resVertical = 1080
dataPointSideLengthRes = 15
colorThreshold = 25

if encode.lower() == "true":
    print("Encoding mode!")
    Encode(inputFilePath, outputVideoPath, color_mapping, frameRate, resHorizontal, resVertical, dataPointSideLengthRes)
else:
    print("Decoding mode!")
    inputVideoPath = inputFilePath
    outputFilePath = outputVideoPath
    Decode(inputVideoPath, outputFilePath, color_mapping, resHorizontal, resVertical, dataPointSideLengthRes, colorThreshold)