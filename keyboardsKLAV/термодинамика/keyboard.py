from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Термодинамика ---------------
def get_thermodynamics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Внутренняя энергия")],
        [KeyboardButton(text="Способы теплопередачи")],
        [KeyboardButton(text="Количество теплоты")],
        [KeyboardButton(text="Плавление, кристаллизация")],
        [KeyboardButton(text="Парообразование, конденсация")],
        [KeyboardButton(text="Сгорание топлива")],
        [KeyboardButton(text="Работа в термодинамике")],
        [KeyboardButton(text="Первый закон термодинамики")],
        [KeyboardButton(text="КПД")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)