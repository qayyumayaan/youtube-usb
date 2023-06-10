from binaryFileConverter import FileToBinary, BinaryToFile
from helper import BinaryToColors, ColorsToBinary
from videoGenerator import ColorsToVideo
from videoDecoder import VideoToColors

binaryPath = r"tempInProcess/binary_form.bin"
colorsPath = r"tempInProcess/colors.txt"
decodedVideoPath = r"tempInProcess/decodedMess.txt"


def Encode(inputFilePath, outputVideoPath):
        
    FileToBinary(inputFilePath, binaryPath)

    BinaryToColors(binaryPath, colorsPath)

    ColorsToVideo(colorsPath, outputVideoPath)
    

def Decode(inputVideoPath, outputFilePath):
    
    VideoToColors(inputVideoPath, decodedVideoPath)

    ColorsToBinary(colorsPath, binaryPath)

    BinaryToFile(binaryPath, outputFilePath)