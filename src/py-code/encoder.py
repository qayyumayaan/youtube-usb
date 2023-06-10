from main import FileToBinary
from helper import BinaryToColors
from videoGenerator import ColorsToVideo

def Encode(inputFilePath, outputVideoPath):
    
    binaryPath = r"tempInProcess/binary_form.bin"
    colorsPath = r"tempInProcess/colors.txt"
    
    FileToBinary(inputFilePath, binaryPath)

    BinaryToColors(binaryPath, colorsPath)

    ColorsToVideo(colorsPath, outputVideoPath)