import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)
data_loader = DataLoader(dataset, batch_size=64, drop_last=True)

class myNN(nn.Module):
    def __init__(self):
        super(myNN, self).__init__()
        self.linear1 = Linear(196608, 10)

    def forward(self, input):
        output = self.linear1(input)
        return output


mynn = myNN()   # 实例化

for data in data_loader:
    imgs, targets = data
    print(type(imgs))
    print(type(targets))
    print(imgs.shape)

    output = torch.reshape(imgs, (1, 1, 1, -1))
    print(output.shape)

    output = mynn(output)
    print(output.shape)