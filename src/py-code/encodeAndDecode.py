import os
from binaryFileConverter import FileToBinary, BinaryToFile
from colorBinaryConverter import BinaryToColors, ColorsToBinary
from videoGenerator import ColorsToVideo
from videoDecoder import VideoToColors

binaryPath = r"tempInProcess/binary_form.bin"
colorsPath = r"tempInProcess/colors.txt"
# decodedVideoPath = r"tempInProcess/decodedMess.txt"


def Encode(inputFilePath, outputVideoPath):
        
    FileToBinary(inputFilePath, binaryPath)

    BinaryToColors(binaryPath, colorsPath)

    ColorsToVideo(colorsPath, outputVideoPath)  

    os.remove(binaryPath)
    os.remove(colorsPath)

    

def Decode(inputVideoPath, outputFilePath):
    
    VideoToColors(inputVideoPath, colorsPath)

    ColorsToBinary(colorsPath, binaryPath)

    BinaryToFile(binaryPath, outputFilePath)

    os.remove(binaryPath)  
    os.remove(colorsPath)
