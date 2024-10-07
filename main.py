import cv2

import matplotlib.pyplot as plt

url = ""
cap = cv2.VideoCapture(url)

# Get the width, height, and frames per second (fps) of the video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object to save the video
output = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if ret:
        # Display the frame
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.pause(0.01)
        plt.clf()

        # Write the frame to the output video file
        output.write(frame)

        # Check for the 'q' key to stop the streaming
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
output.release()

# Close the plot window
plt.close()
