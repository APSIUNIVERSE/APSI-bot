from aiogram.fsm.state import StatesGroup, State

class FigmaTask(StatesGroup):
    Brief = State()
    Number = State()

class TildaTask(StatesGroup):
    Brief = State()
    Number = State()

class BotTask(StatesGroup):
    Brief = State()
    Number = State()