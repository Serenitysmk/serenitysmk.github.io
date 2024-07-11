# import cv2
# import numpy as np

# in_vid = "images/auv_mapping.mp4"
# out_vid = "images/auv_mapping_small.mp4"


# H, W = 720, 1280
# H_new, W_new = int(H), int(W)

# cap = cv2.VideoCapture(in_vid)

# codec_code = cap.get(cv2.CAP_PROP_FOURCC)

# print(codec_code)

# writer = cv2.VideoWriter(
#         out_vid, cv2.VideoWriter_fourcc('H', '2', '6', '4'), 10, (W_new, H_new))

# cnt = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     if cnt % 10 == 0:
#         newframe = cv2.resize(frame, (W_new, H_new))

#         writer.write(newframe)

#         cv2.imshow("frame", frame)
#         cv2.waitKey(5)
#         if cv2.waitKey(1) == ord('q'):
#             break

#     cnt += 1
# cap.release()

from moviepy.editor import *

in_vid = "images/bubblebox.mp4"
out_vid = "images/bubblebox_small.mp4"

clip = VideoFileClip(in_vid)

new_clip = clip.set_fps(20)
new_clip = new_clip.fx(vfx.speedx, 2)
new_clip.write_videofile(out_vid)