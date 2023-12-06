import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader

data_set = torchvision.datasets.CIFAR10("./dataset",
                                        train=True,
                                        transform=torchvision.transforms.ToTensor(),
                                        download=True)

data_loader = DataLoader(data_set, batch_size=64)


class myNN(nn.Module):
    def __init__(self):
        super(myNN, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x


mynn = myNN()
# print(mynn)

for data in data_loader:
    imgs_, targets = data
    output_ = mynn(imgs_)
    print(output_.shape)
