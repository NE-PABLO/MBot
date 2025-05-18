from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Динамика
def get_dinamika_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Плотность вещества")],
        [KeyboardButton(text="Равнодействующая сил")],
        [KeyboardButton(text="Первый закон Ньютона")],
        [KeyboardButton(text="Второй закон Ньютона")],
        [KeyboardButton(text="Третий закон Ньютона")],
        [KeyboardButton(text="Сила трения")],
        [KeyboardButton(text="Сила упругости")],
        [KeyboardButton(text="Закон всемирного тяготения")],
        [KeyboardButton(text="Сила тяжести")],
        [KeyboardButton(text="Сила нормального давления, если тело покоится (движется равномерно)")],
        [KeyboardButton(text="Сила нормального давления, если телодвижется с ускорением, направленным вверх")],
        [KeyboardButton(text="Сила нормального давления, если телодвижется с ускорением, направленным вниз")],
        [KeyboardButton(text="Вес тела")],
        [KeyboardButton(text="Первая космическая скорость")],
        [KeyboardButton(text="Вторая космическая скорость")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)