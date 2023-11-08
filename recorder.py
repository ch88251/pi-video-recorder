import cv2

# Open a connection to the USB camera (usually /dev/video0)
cap = cv2.VideoCapture(0)

# Set the video resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Write the frame to the output video file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and the video writer
cap.release()
out.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

