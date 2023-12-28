'''
修改已有的网络模型
'''

import torchvision

# train_data = torchvision.datasets.ImageNet("./dataset/image_net", split='train', download=True, transform=torchvision.transforms.ToTensor())
from torch import nn

vgg16_false = torchvision.models.vgg16(pretrained=False)    # 其中参数是默认值

vgg16_true = torchvision.models.vgg16(pretrained=True)      # 其中参数已经经过数据集的训练

# train_data = torchvision.datasets.CIFAR10('./dataset', train=True, transform=torchvision.transforms.ToTensor(), download=True)

print(vgg16_true)
vgg16_true.classifier.add_module('add_linear', nn.Linear(1000, 10)) # 在vgg16网络clasifier层的最后添加线性层
print(vgg16_true)

print(vgg16_false)
vgg16_false.classifier[6] = nn.Linear(4096, 10, bias=True)  # 把vgg16网络classifier层最后一层的参数修改
print(vgg16_false)

