import cv2

video = cv2.VideoCapture("E:\\WJH's_Backup\\YOGA_Backup\\Learn_Python\\CV2\\output.mp4")

# 检查视频是否成功打开
if not video.isOpened():
    print("无法打开视频文件")
    exit()

frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)