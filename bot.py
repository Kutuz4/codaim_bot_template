#!/usr/bin/python3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers import welcome, image_handler, question_answer, question_answer_tochno
from bot.states import States

bot = Bot(token="add_your_token_here")
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(welcome, commands=["start"], state="*")
dp.register_message_handler(image_handler, state=States.image, content_types="photo")
dp.register_message_handler(question_answer, state=States.work)
dp.register_message_handler(question_answer_tochno, state=States.question)

if __name__ == "__main__":
    executor.start_polling(dp)
