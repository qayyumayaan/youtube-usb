import cv2
import numpy as np
from PIL import Image

# Mapping of characters to GBR colors
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
colorsFilePath = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\colors.txt"

def videoCreator():
    totalPixels = resHorizontal * resVertical
    numPixelsPerFrame = int(totalPixels / (dataPointSideLengthRes**2))

    # height = int(resVertical / dataPointSideLengthRes)
    width = int(resHorizontal / dataPointSideLengthRes)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('converted.mp4', fourcc, frameRate, (resHorizontal, resVertical))

    with open(colorsFilePath, 'r') as f:
        colors = f.read().replace('\n', '')

    for i in range(0, len(colors), numPixelsPerFrame):
        frame = np.zeros((resVertical, resHorizontal, 3), dtype=np.uint8)

        for j in range(numPixelsPerFrame):
            if i + j >= len(colors):
                break

            color = color_mapping[colors[i+j]]
            
            start_row = (j // width) * dataPointSideLengthRes
            end_row = start_row + dataPointSideLengthRes
            start_col = (j % width) * dataPointSideLengthRes
            end_col = start_col + dataPointSideLengthRes

            frame[start_row:end_row, start_col:end_col] = color

        video.write(frame)

    video.release()

    print("Finished converting!")

videoCreator()