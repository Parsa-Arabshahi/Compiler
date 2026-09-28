import torch
import torch.nn as nn

class TransformerEncoder(nn.Module):

    def __init__(self):
        super(TransformerEncoder, self).__init__()

        self.attn = nn.MultiheadAttention(embed_dim=128, num_heads=8, batch_first=True)
        self.drop1 = nn.Dropout(p=0.1)
        self.norm1 = nn.LayerNorm(128)
        self.ff1 = nn.Linear(in_features=128, out_features=512)
        self.gelu1 = nn.GELU()
        self.drop2 = nn.Dropout(p=0.1)
        self.ff2 = nn.Linear(in_features=512, out_features=128)
        self.norm2 = nn.LayerNorm(128)
        self.out = nn.Flatten(start_dim=0, end_dim=1)

    def forward(self, x):
        attn = self.attn(x, x, x)[0]
        drop1 = self.drop1(attn)
        norm1 = self.norm1(drop1 + x)
        ff1 = self.ff1(norm1)
        gelu1 = self.gelu1(ff1)
        drop2 = self.drop2(gelu1)
        ff2 = self.ff2(drop2)
        norm2 = self.norm2(ff2 + norm1)
        out = self.out(norm2)

        return out


if __name__ == '__main__':
    device = torch.device('cpu')
    model = TransformerEncoder().to(device)
    x = torch.randn(1, 512, 128).to(device)

    y = model(x)

    print(y)
    print(y.shape)