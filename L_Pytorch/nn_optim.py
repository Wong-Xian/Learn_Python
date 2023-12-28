import torch
import torchvision
from torch import nn
from torch.nn import Sequential, Conv2d, MaxPool2d, Flatten, Linear
from torch.utils.data import DataLoader

ds = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor(), download=True)

dl = DataLoader(dataset=ds, batch_size=1)


class MyNN(nn.Module):
    def __init__(self):
        super(MyNN, self).__init__()
        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2),
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


loss = nn.CrossEntropyLoss()
mynn = MyNN()
optim = torch.optim.SGD(mynn.parameters(), lr=0.01)

for epoch in range(20):
    running_loss = 0.0
    for data in dl:
        imgs, target = data
        outputs = mynn(imgs)
        result_loss = loss(outputs, target)
        optim.zero_grad()
        result_loss.backward()
        optim.step()
        running_loss += result_loss
    print(running_loss)
