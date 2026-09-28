import torch
import torch.nn as nn

class InceptionBlock(nn.Module):

    def __init__(self):
        super(InceptionBlock, self).__init__()

        self.convA1 = nn.Conv2d(in_channels=32, out_channels=16, kernel_size=1, stride=1, padding=0)
        self.reluA = nn.ReLU()
        self.convB1 = nn.Conv2d(in_channels=32, out_channels=16, kernel_size=1, stride=1, padding=0)
        self.convB2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.reluB = nn.ReLU()
        self.cat1 = nn.Identity()
        self.bn1 = nn.BatchNorm2d(48)
        self.out = nn.ReLU()

    def forward(self, x):
        convA1 = self.convA1(x)
        convB1 = self.convB1(x)
        reluA = self.reluA(convA1)
        convB2 = self.convB2(convB1)
        reluB = self.reluB(convB2)
        cat1 = torch.cat([reluA, reluB], dim=1)
        bn1 = self.bn1(cat1)
        out = self.out(bn1)

        return out


if __name__ == '__main__':
    device = torch.device('cpu')
    model = InceptionBlock().to(device)
    x = torch.randn(1, 32, 56, 56).to(device)

    y = model(x)

    print(y)
    print(y.shape)