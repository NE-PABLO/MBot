from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Электродинамика ---------------
def get_electrodynamics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Электрическое поле")],
        [KeyboardButton(text="Законы постоянного тока")],
        [KeyboardButton(text="Магнитное поле и электромагнитная индукция")],
        [KeyboardButton(text="Электромагнитные колебания и волны")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)