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

numPixels = 144
height = 9
width = 16

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('converted.mp4', fourcc, 30.0, (1920, 1080))

with open('colors1.txt', 'r') as f:
    colors = f.read().replace('\n', '')

for i in range(0, len(colors), numPixels):
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)

    for j in range(numPixels):
        if i + j >= len(colors):
            break

        color = color_mapping[colors[i+j]]
        
        start_row = (j // height) * 120
        end_row = start_row + 120
        start_col = (j % width) * 120
        end_col = start_col + 120

        frame[start_row:end_row, start_col:end_col] = color

    video.write(frame)

# Release the video writer
video.release()

print("Finished converting!")
