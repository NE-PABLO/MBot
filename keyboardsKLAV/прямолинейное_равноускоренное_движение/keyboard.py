from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# равноускореное
def get_ravnoyskorenoe_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Ускорение при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="Скорость при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="Проекция перемещения при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="Зависимость координаты от времени при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="График зависимости проекции ускорения от времени при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="График зависимости проекции скорости от времени при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="График зависимости координаты от времени при равноускоренном прямолинейном движении")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)