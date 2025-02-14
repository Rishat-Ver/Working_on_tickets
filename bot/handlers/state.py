from aiogram.fsm.state import State, StatesGroup


class AddProfessionState(StatesGroup):
    waiting_for_profession_name = State()