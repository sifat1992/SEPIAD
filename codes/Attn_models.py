# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:31:45 2025

@author: szk9
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

## Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

#SE==============================================================================================================

class SEAttention(nn.Module):
    def __init__(self, channel,reduction=8):   
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)
    
 

