from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):

    work = State()
    question = State()
    image = State()