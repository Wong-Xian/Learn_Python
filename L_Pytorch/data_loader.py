import torchvision
from torch.utils.data import DataLoader

testdata = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor())
test_loader = DataLoader(dataset=testdata, batch_size=4, shuffle=True, num_workers=0, drop_last=False)

for data in test_loader:
    imgs, targets = data
    print(imgs.shape)
    print(targets)
    