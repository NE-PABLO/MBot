from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Механические колебания и волны -------------------
def get_mechanicheskie_kolebaniya_i_volny_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Амплитуда колебаний")],
        [KeyboardButton(text="Период колебаний")],
        [KeyboardButton(text="Частота колебаний")],
        [KeyboardButton(text="Гармонические колебания")],
        [KeyboardButton(text="Циклическая частота")],
        [KeyboardButton(text="Уравнение гармонических колебаний")],
        [KeyboardButton(text="Закон сохранения энергии для математического маятника")],
        [KeyboardButton(text="Закон сохранения энергии для пружинного маятника")],
        [KeyboardButton(text="Период колебаний математического маятника")],
        [KeyboardButton(text="Период колебаний пружинного маятника")],
        [KeyboardButton(text="Длина волны")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)