import numpy as np
import cv2
import torch
from torchvision.transforms import Resize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def prepare_image(path):

    image = cv2.imread(path).transpose((2, 0, 1))
    image = torch.from_numpy(image).float()

    return image

def form_reply_keyboard(buttons_info):
    keyboard = ReplyKeyboardMarkup()

    for i in range(len(buttons_info)):
        print(buttons_info[i])
        keyboard.add(KeyboardButton(str(buttons_info[i])))
        
    return keyboard
