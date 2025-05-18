from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Свободное падение
def get_svobodnoe_padenie_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Свободное падение тела по вертикали")],
        [KeyboardButton(text="Движение тела по вертикали вниз")],
        [KeyboardButton(text="Движение тела по вертикали вверх")],
        [KeyboardButton(text="Проекции скорости при движении тела, брошенного под углом к горизонту")],
        [KeyboardButton(text="Уравнения координат при движении тела, брошенного под углом к горизонту")],
        [KeyboardButton(text="Время полета при движении тела, брошенного под углом к горизонту")],
        [KeyboardButton(text="Дальность полета при движении тела, брошенного под углом к горизонту")],
        [KeyboardButton(text="Максимальная высота подъёма при движении тела, брошенного под углом к горизонту")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)