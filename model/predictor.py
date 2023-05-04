import torch
from torch import nn
from torchvision.transforms import Resize


class MyModel:

    def __init__(self, path=None):
        if path is None:
            self.resizer = Resize((256, 256))
            self.my_model = nn.Sequential(
                nn.Conv2d(3, 1, kernel_size=3, padding=(1, 1)), 
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2),
                nn.Flatten(),
                )
            
            self.linear_head = nn.Sequential(
                nn.Linear(16384, 1),
                nn.Sigmoid()
                )

    
    def __call__(self, data: torch.FloatTensor, is_positive=True):

        if len(data.shape) == 3:
            data = data.view(1, *data.shape)

        if data.max() > 2:
            data /= 255

        with torch.no_grad():
            resized_data = self.resizer(data)
            prediction = self.my_model(resized_data)
            
            return (2 * is_positive - 1) * self.linear_head(prediction)[0].item()
    
model = MyModel()