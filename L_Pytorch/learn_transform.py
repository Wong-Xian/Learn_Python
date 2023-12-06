from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

'''
transforms.py 文件 类似工具箱，把特定格式图片转换成 tensor 格式
    ToTensor    工具
    resize      工具

tensor 数据类型
'''

img_path = "hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")  # 创建 log 对象

# 使用方法
img_trans = transforms.ToTensor()
img_tensor = img_trans(img)

writer.add_image("tensor img", img_tensor)  # 添加图片
writer.close()  # 关闭

# print(type(img_trans))
# print(type(img_tensor))