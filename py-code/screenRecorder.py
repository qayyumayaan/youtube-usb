import pyautogui
import cv2
import numpy as np

# Set the resolution and output file name
screen_size = (1920, 1080)
output_file = 'screen_record.avi'

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, 20.0, screen_size)

try:
    while True:
        # Capture the screen and convert the image to BGR format
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Write the frame to the output file
        out.write(frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # Release the VideoWriter and close the OpenCV windows
    out.release()
    cv2.destroyAllWindows()
