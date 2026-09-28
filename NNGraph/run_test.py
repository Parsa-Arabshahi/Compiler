import torch
from output import MLP

model = MLP()

x = torch.randn(1, 784)

y = model(x)

print(y)
print(y.shape)