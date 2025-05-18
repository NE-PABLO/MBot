from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Поиск")],
        [KeyboardButton(text="Экзамены")], # Добавлена кнопка "Экзамены"
        [KeyboardButton(text="🎤 Ваш мега-коммент")],
        [KeyboardButton(text="Механика")],
        [KeyboardButton(text="Молекулярная физика")],
        [KeyboardButton(text="Термодинамика")],
        [KeyboardButton(text="Электродинамика")],
        [KeyboardButton(text="Оптика")],
        [KeyboardButton(text="Квантовая физика")],
        [KeyboardButton(text="Ядерная физика")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
