import torch
import torch.nn.functional as F

input_ = torch.tensor(
    [[1,2,0,3,1],
     [0,1,2,3,1],
     [1,2,1,0,0],
     [5,2,3,1,1],
     [2,1,0,1,1]]
)

kernel = torch.tensor(
    [[1,2,1],
     [0,1,0],
     [2,1,0]]
)

print("before reshape")
print(input_.shape)
print(kernel.shape)

input_ = torch.reshape(input_, (1, 1, input_.shape[0], input_.shape[1]))
kernel = torch.reshape(kernel, (1, 1, kernel.shape[0], kernel.shape[1]))

print("\nafter reshape")
print(input_.shape)
print(kernel.shape)

output_ = F.conv2d(input_, kernel, stride=1)
print("\n", output_)

output_2 = F.conv2d(input_, kernel, stride=1, padding=1)    # padding 在input周围添加一列数据，默认为1，再进行卷积
print("\n", output_2)