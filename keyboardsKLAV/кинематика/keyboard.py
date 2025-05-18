from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Механика_Кинематика -----------------
def get_kinematics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Прямолинейное равномерное движение")],
        [KeyboardButton(text="Прямолинейное равноускоренное движение")],
        [KeyboardButton(text="Средняя скорость")],
        [KeyboardButton(text="Свободное падение")],
        [KeyboardButton(text="Движение по окружности")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)