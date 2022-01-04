# importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
#Now, before recording the screen, we have to create a VideoWriter object. Also, we have to specify the output file name, Video codec, FPS, and video resolution. In video codec, we have to specify a 4-byte code (such as XVID, MJPG, X264, etc.). We’ll be using XVID here.
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = r"D:\Rama\Portofolio Rama\Recording.avi"

# Specify frames rate. We can choose
# any value and experiment with it
fps = 60.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
