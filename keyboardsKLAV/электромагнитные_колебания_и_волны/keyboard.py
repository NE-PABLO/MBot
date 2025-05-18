from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Электродинамика_Электромагнитные колебания и волны ---------------
def get_electromagnetic_oscillations_and_waves_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Колебательный контур")],
        [KeyboardButton(text="Уравнения колебаний в колебательном контуре")],
        [KeyboardButton(text="Формула Томсона")],
        [KeyboardButton(text="Циклическая частота электромагнитных колебаний")],
        [KeyboardButton(text="Связь  заряда с силой тока")],
        [KeyboardButton(text="Закон сохранения энергии в контуре")],
        [KeyboardButton(text="Шкала электромагнитных волн")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)