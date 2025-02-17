from aiogram.fsm.state import State, StatesGroup


class AddProfessionState(StatesGroup):
    waiting_for_profession_name = State()


class AddTicketState(StatesGroup):
    waiting_for_keys_hour = State()
    waiting_for_profession = State()


class GetHoursState(StatesGroup):
    waiting_for_start_date = State()