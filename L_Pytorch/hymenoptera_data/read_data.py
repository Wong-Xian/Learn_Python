from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):  # 类
    def __init__(self, root_dir, label_dir):    # 类构造函数
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        return img, img_name

root_dir = "/learn_pytorch/hymenoptera_data/train"
ants_dir = "ants"
bees_dir = "bees"

# 实例化 蚂蚁 数据集
ants_dataset = MyData(root_dir, ants_dir)
img, name = ants_dataset.__getitem__(1)
img.show()
print(name)

# 实例化 蜜蜂 数据集
bees_dataset = MyData(root_dir, bees_dir)
