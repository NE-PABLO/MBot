from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# равномерное
def get_ravnomernoe_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Скорость прямолинейного равномерного движения")],
        [KeyboardButton(text="Перемещение при равномерном движении")],
        [KeyboardButton(text="Зависимость координаты от времени при равномерном прямолинейном движении")],
        [KeyboardButton(text="График зависимости координаты от времени при равномерном прямолинейном движении")],
        [KeyboardButton(text="Графики зависимости проекции скорости от времени при равномерном прямолинейном движении")],
        [KeyboardButton(text="Графики зависимости проекции перемещения от времени")],
        [KeyboardButton(text="Графики зависимости пути от времени при равномерном прямолинейном движении")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
