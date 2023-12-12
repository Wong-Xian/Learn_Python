import numpy as np
import cv2 as cv

vCap = cv.VideoCapture(1)  # 打开默认摄像头

# 错误控制
if not vCap.isOpened():
    print("open error")
    exit(-1)

while True:
    ret, frame = vCap.read()  # capture frame

    if not ret:
        print("Can't read frame.")
        break

    # 获取帧率
    fps = vCap.get(cv.CAP_PROP_FPS)
    cv.putText(frame, 'frame: '+str(fps), (10, 20),
        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # 获取图像长宽
    H, W, C = frame.shape
    half_w = int(W/2)
    frame_L = frame[0:H, 0:half_w]
    frame_R = frame[0:H, half_w:W]
    cv.putText(frame, 'H:'+str(H)+' W:'+str(W)+' C:'+str(C),
        (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5,  (255, 0, 0), 1)  

    # 显式原始图像
    # cv.imshow("origin frame", frame)
    cv.imshow("frame_left", frame_L)
    cv.imshow("frame_right", frame_R)

    if cv.waitKey(1) == ord('q'):
        break

vCap.release()
cv.destroyAllWindows()
