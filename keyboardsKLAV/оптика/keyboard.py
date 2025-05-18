from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Оптика ---------------
def get_optics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Закон прямолинейного распространения света")],
        [KeyboardButton(text="Закон отражения света")],
        [KeyboardButton(text="Закон преломления света")],
        [KeyboardButton(text="Оптическая сила линзы")],
        [KeyboardButton(text="Формула линзы")],
        [KeyboardButton(text="Интерференция света")],
        [KeyboardButton(text="Формула дифракционной решетки")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)