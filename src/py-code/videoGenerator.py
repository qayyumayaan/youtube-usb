import cv2
import numpy as np
from PIL import Image

# Mapping of characters to RGB colors
color_mapping = {
    'D': (0, 0, 0),     # black
    'B': (0, 0, 255),   # blue
    'G': (0, 255, 0),   # green
    'C': (0, 255, 255), # cyan
    'R': (255, 0, 0),   # red
    'P': (128, 0, 128), # purple
    'Y': (255, 255, 0), # yellow
    'W': (255, 255, 255)# white
}

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('converted.mp4', fourcc, 30.0, (1920, 1080))

with open('colors.txt', 'r') as f:
    colors = f.read().replace('\n', '')

for i in range(0, len(colors), 144):
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)

    for j in range(144):
        if i + j >= len(colors):
            break

        color = color_mapping[colors[i+j]]
        
        start_row = (j // 12) * 120
        end_row = start_row + 120
        start_col = (j % 12) * 120
        end_col = start_col + 120

        frame[start_row:end_row, start_col:end_col] = color

    video.write(frame)

# Release the video writer
video.release()
