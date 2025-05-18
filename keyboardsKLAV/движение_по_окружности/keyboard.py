from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Равномерное движение по окружности -----------------
def get_ravnomernoe_dvizhenie_po_okruzhnosti_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Скорость при равномерном движении по окружности")],
        [KeyboardButton(text="Формула связи периода и частоты")],
        [KeyboardButton(text="Центростремительное ускорение")],
        [KeyboardButton(text="Угловая скорость")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)