import torch
import torch.nn as nn

class ResBlock(nn.Module):

    def __init__(self):
        super(ResBlock, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.skip = nn.Identity()
        self.relu2 = nn.ReLU()
        self.out = nn.Flatten(start_dim=1, end_dim=-1)

    def forward(self, x):
        conv1 = self.conv1(x)
        bn1 = self.bn1(conv1)
        relu1 = self.relu1(bn1)
        conv2 = self.conv2(relu1)
        bn2 = self.bn2(conv2)
        skip = bn2 + x
        relu2 = self.relu2(skip)
        out = self.out(relu2)

        return out


if __name__ == '__main__':
    device = torch.device('cpu')
    model = ResBlock().to(device)
    x = torch.randn(1, 64, 32, 32).to(device)

    y = model(x)

    print(y)
    print(y.shape)