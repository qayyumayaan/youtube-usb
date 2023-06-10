import os
from binaryFileConverter import FileToBinary, BinaryToFile
from colorBinaryConverter import BinaryToColors, ColorsToBinary
from videoGenerator import ColorsToVideo
from videoDecoder import VideoToColors

binaryPath = r"binary_form.bin"
colorsPath = r"colors.txt"


def Encode(inputFilePath, outputVideoPath, color_mapping, frameRate, resHorizontal, resVertical, dataPointSideLengthRes):
        
    FileToBinary(inputFilePath, binaryPath)

    BinaryToColors(binaryPath, colorsPath)

    ColorsToVideo(colorsPath, outputVideoPath, color_mapping, frameRate, resHorizontal, resVertical, dataPointSideLengthRes)

    os.remove(binaryPath)
    os.remove(colorsPath)

    

def Decode(inputVideoPath, outputFilePath, color_mapping, resHorizontal, resVertical, dataPointSideLengthRes, colorThreshold):
    
    VideoToColors(inputVideoPath, colorsPath, color_mapping, resHorizontal, resVertical, dataPointSideLengthRes, colorThreshold)

    ColorsToBinary(colorsPath, binaryPath)

    BinaryToFile(binaryPath, outputFilePath)

    os.remove(binaryPath)  
    os.remove(colorsPath)
