from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Молекулярная физика -------
def get_molekylarn_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Количество вещества")],
        [KeyboardButton(text="Основные положения МКТ")],
        [KeyboardButton(text="Диффузия")],
        [KeyboardButton(text="Идеальный газ")],
        [KeyboardButton(text="Основное уравнение МКТ идеального газа")],
        [KeyboardButton(text="Связь температуры газа со средней кинетической энергией")],
        [KeyboardButton(text="Уравнение Менделеева-Клапейрона")],
        [KeyboardButton(text="Внутренняя энергия одноатомного идеального газа")],
        [KeyboardButton(text="Изотермический процесс")],
        [KeyboardButton(text="Относительная влажность")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)