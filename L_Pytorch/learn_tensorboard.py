from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")  # 创建 log

img_path = "hymenoptera_data/train/ants/0013035.jpg"  # 相对地址
img_PIL = Image.open(img_path)  # 用 PIL 打开图像
img_np = np.array(img_PIL)      # 把 PIL 格式转换成 np 格式



writer.add_image("test", img_np, 1, dataformats='HWC')

writer.close()