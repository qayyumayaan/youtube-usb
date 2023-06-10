import cv2
import numpy as np

def ColorsToVideo(colorsFilePath, outputVideoPath, color_mapping, frameRate, resHorizontal, resVertical, dataPointSideLengthRes):  

    totalPixels = resHorizontal * resVertical
    numPixelsPerFrame = int(totalPixels / (dataPointSideLengthRes**2))

    width = int(resHorizontal / dataPointSideLengthRes)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(outputVideoPath, fourcc, frameRate, (resHorizontal, resVertical))

    # Sequence to append at the beginning
    # sequence = "eDRGYBPCWe"

    with open(colorsFilePath, 'r') as f:
        colors = f.read().replace('\n', '')

    # colors = sequence + colors 

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

    print("Finished generating the video!")
