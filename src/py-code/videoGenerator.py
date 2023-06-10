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
totalPixels = resHorizontal * resVertical
# totalPixels = 2073600

dataPointSideLengthResolution = 120


numPixelsPerFrame = int(totalPixels / (dataPointSideLengthResolution**2))
# numPixelsPerFrame = 144

height = int(resVertical / dataPointSideLengthResolution)
width = int(resHorizontal / dataPointSideLengthResolution)

print(numPixelsPerFrame, height, width)

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('converted.mp4', fourcc, frameRate, (resHorizontal, resVertical))

with open('colors1.txt', 'r') as f:
    colors = f.read().replace('\n', '')

for i in range(0, len(colors), numPixelsPerFrame):
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)

    for j in range(numPixelsPerFrame):
        if i + j >= len(colors):
            break

        color = color_mapping[colors[i+j]]
        
        start_row = (j // width) * dataPointSideLengthResolution
        end_row = start_row + dataPointSideLengthResolution
        start_col = (j % width) * dataPointSideLengthResolution
        end_col = start_col + dataPointSideLengthResolution

        frame[start_row:end_row, start_col:end_col] = color

    video.write(frame)

# Release the video writer
video.release()

print("Finished converting!")
