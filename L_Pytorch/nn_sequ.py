import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Linear, Sequential
from torch.nn.modules.flatten import Flatten
from torch.utils.tensorboard import SummaryWriter


class myNN(nn.Module):
    def __init__(self):
        super(myNN, self).__init__()

        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2, stride=1),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, x):
        x = self.model1(x)
        return x

mynn = myNN()
in_ = torch.ones((64, 3, 32, 32))
out_ = mynn(in_)
print(out_.shape)

writer = SummaryWriter("log_seq")
writer.add_graph(mynn, in_)
writer.close()