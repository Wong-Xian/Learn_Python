import torch
from torch import nn
from torch.nn import MaxPool2d
import torchvision as tv
from torch.utils.data import DataLoader as DL
from torch.utils.tensorboard import SummaryWriter as SW

# 创建【数据集】对象
dataset = tv.datasets.CIFAR10("./dataset", train=False, download=True, transform=tv.transforms.ToTensor())

# 创建【用于载入数据集】的对象
data_loader = DL(dataset, batch_size=64)

# 创建【写log】的对象
logger = SW("log_maxpooling")


class myNN(nn.Module):                                              # 定义自己的NN类，继承自 nn.Module
    def __init__(self):                                             # 构造函数 初始化
        super(myNN, self).__init__()                                # 调用父类构造函数，使子类有父类的属性
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=True)    # 该类具有 maxpool1 属性

    def forward(self, input_):                                      # 重写forward
        output_ = self.maxpool1(input_)
        # 能这么用是因为【MaxPool2d类】继承自【_MaxPoolNd类】继承自【Module类】，Module类有__call__函数
        return output_

mynn = myNN()

step =0

for data in data_loader:
    img, target = data
    logger.add_images("input", img, step)
    outputs = mynn(img)
    logger.add_images("otput", outputs, step)
    step += 1


logger.close()