import torchvision

data_trans = torchvision.transforms.ToTensor()  # 实例化 to tensor 对象          用于此 ↓
train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, transform=data_trans, download=True)

print(train_set[0])

# test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True)