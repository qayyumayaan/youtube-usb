import cv2
import numpy as np

def distance(color1, color2):
    return np.sqrt(sum([(a - b) ** 2 for a, b in zip(color1, color2)]))

def closestColorMapping(color, colorThreshold, color_mapping):
    min_distance = float('inf')
    closest_color = None

    for char, defined_color in color_mapping.items():
        dist = distance(color, defined_color)
        if dist < min_distance:
            min_distance = dist
            closest_color = char

    if min_distance <= colorThreshold:
        return closest_color
    else:
        return None

def VideoToColors(inputVideoPath, colorsPath, color_mapping, resHorizontal, resVertical, dataPointSideLengthRes, colorThreshold):
    width = int(resHorizontal / dataPointSideLengthRes)
    height = int(resVertical / dataPointSideLengthRes)

    video = cv2.VideoCapture(inputVideoPath)

    color_string = ''

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        for i in range(height):
            for j in range(width):
                center_row = i * dataPointSideLengthRes + dataPointSideLengthRes // 2
                center_col = j * dataPointSideLengthRes + dataPointSideLengthRes // 2

                if center_row < frame.shape[0] and center_col < frame.shape[1]:
                    color = tuple(frame[center_row, center_col])
                    char = closestColorMapping(color, colorThreshold, color_mapping)

                    if char is not None:
                        color_string += char
                    else:
                        print(f"Warning: No character mapping for color {color}")

    video.release()
    
    with open(colorsPath, 'w') as file:
        file.write(color_string)

    print("Finished decoding the video!")


