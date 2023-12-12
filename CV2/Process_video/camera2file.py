import cv2
from datetime import datetime

# 打开摄像头
camera = cv2.VideoCapture(1)

# 设置录制参数
date = str(datetime.now())   # 获取日期
output_file = "E:\\WJH's_Backup\\YOGA_Backup\\Learn_Python\\CV2\\Process_video\\a.mp4"   # 以日期命名

# 创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = float(camera.get(cv2.CAP_PROP_FPS))
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(filename=output_file, fourcc=fourcc, fps=fps, frameSize=(width, height))

# 开始录制视频
while camera.isOpened():
    ret, frame = camera.read()

    if ret:
        # 对帧进行处理，例如添加文本或绘图
        # cv2.putText(frame, 'Hello, World!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 将帧写入输出视频文件
        out.write(frame)

        # 显示处理后的帧
        cv2.imshow('frame', frame)

        # 按'q'键退出录制
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放VideoWriter对象和摄像头/视频文件
out.release()
camera.release()

# 关闭所有窗口
cv2.destroyAllWindows()
