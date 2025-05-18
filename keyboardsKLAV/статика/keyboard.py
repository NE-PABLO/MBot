from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Статика -------------------
def get_statika_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Момент силы")],
        [KeyboardButton(text="Условие равновесия рычага")],
        [KeyboardButton(text="Условия равновесия твердого тела в ИСО")],
        [KeyboardButton(text="Неподвижный блок")],
        [KeyboardButton(text="Подвижный блок")],
        [KeyboardButton(text="Коэффициент полезного действия или КПД")],
        [KeyboardButton(text="Гидростатическое давление")],
        [KeyboardButton(text="Закон Паскаля")],
        [KeyboardButton(text="Закон Архимеда")],
        [KeyboardButton(text="Условие плавания тел")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)