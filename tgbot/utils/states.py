from aiogram.fsm.state import State, StatesGroup


class AddFunds(StatesGroup):
    sum = State()

class InputData(StatesGroup):
    inputing = State()

class InputAdminPrice(StatesGroup):
    inputing = State()
