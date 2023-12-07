import torch
from torch.nn import ReLU, Sigmoid

input_ = torch.tensor(
    [[-1, 0.1],
     [5, -0.4]]
)

relu = ReLU()
sigm = Sigmoid()

output1 = relu(input_)
output2 = sigm(input_)

print(output1)
print(output2)