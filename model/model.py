import torch
from torch import nn


class MyModel:

    def __init__(self, path=None):
        if path is None:
            self.my_model = nn.Sequential(
                nn.Conv2d(3, 1, kernel_size=3, padding=True), 
                nn.Flatten(),
                nn.Linear(256 * 256, 1)
                )

    
    def __call__(self, data: torch.FloatTensor):

        if len(data.shape) == 3:
            data = data.view(1, *data.shape)

        prediction = self.my_model(data)

        return prediction[0]