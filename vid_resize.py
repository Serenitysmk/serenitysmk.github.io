import cv2
import numpy as np

in_vid = "images/macal.mp4"
out_vid = "images/macal_resize.mp4"


H, W = 1376, 2064
H_new, W_new = int(H/4), int(W/4)

cap = cv2.VideoCapture(in_vid)

writer = cv2.VideoWriter( 
        out_vid, cv2.VideoWriter_fourcc(*'mp4v'), 30, (W_new, H_new))

cnt = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if cnt % 2 == 0:
        newframe = cv2.resize(frame, (W_new, H_new))

        writer.write(newframe)

        cv2.imshow("frame", frame)
        cv2.waitKey(5)
        if cv2.waitKey(1) == ord('q'):
            break

    cnt += 1
cap.release()
