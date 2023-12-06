from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

img = Image.open("hymenoptera_data/train/ants/0013035.jpg")
writter = SummaryWriter("logs")

# to tensor
trans_tensor = transforms.ToTensor()
img_tensor = trans_tensor(img)
writter.add_image("To Tensor", img_tensor)

# normalize
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])# 分别表示三个通道的平均值和标准差
img_norm = trans_norm(img_tensor)
writter.add_image("Normalize", img_norm)

# resize
print(img.size)
trans_resize = transforms.Resize((512, 512))    # 压缩
img_resize = trans_resize(img)          # PIL类型
img_resize = trans_tensor(img_resize)   # 转换完是 tensor 类型
writter.add_image("resize", img_resize, 0)
# print(img_resize)

# Compose


writter.close()
