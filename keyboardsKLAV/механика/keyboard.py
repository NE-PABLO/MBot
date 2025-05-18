from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Механика -----------------
def get_mechanics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Кинематика")],
        [KeyboardButton(text="Динамика")],
        [KeyboardButton(text="Законы сохранения в механике")],
        [KeyboardButton(text="Статика")],
        [KeyboardButton(text="Механические колебания и волны")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)