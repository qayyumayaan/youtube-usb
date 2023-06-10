import cv2
import numpy as np

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

# Inverse color mapping
inverse_color_mapping = {v: k for k, v in color_mapping.items()}

resHorizontal = 1920
resVertical = 1080
dataPointSideLengthRes = 120

# Inverse color mapping
inverse_color_mapping = {v: k for k, v in color_mapping.items()}

def videoReader():
    width = int(resHorizontal / dataPointSideLengthRes)
    height = int(resVertical / dataPointSideLengthRes)

    video = cv2.VideoCapture('converted.mp4')

    color_string = ''

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        for i in range(height):
            for j in range(width):
                start_row = i * dataPointSideLengthRes
                start_col = j * dataPointSideLengthRes

                # To prevent index out of bound, consider the minimum of the end_row/end_col or image dimensions
                end_row = min(start_row + dataPointSideLengthRes, resVertical)
                end_col = min(start_col + dataPointSideLengthRes, resHorizontal)
                
                # Ensure that we're within the frame boundaries
                if end_row <= frame.shape[0] and end_col <= frame.shape[1]:
                    color = tuple(frame[start_row, start_col])
                    char = inverse_color_mapping.get(color)

                    if char is not None:
                        color_string += char
                    else:
                        print(f"Warning: No character mapping for color {color}")

    video.release()

    return color_string

decodedMessPath = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\decodedMess.txt"


with open(decodedMessPath, 'w') as file:
    file.write(videoReader())