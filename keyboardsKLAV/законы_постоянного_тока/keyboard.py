from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Электродинамика_Законы постоянного тока ---------------
def get_zakon_postoinogo_toka_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Сила тока")],
        [KeyboardButton(text="Электрическое сопротивление")],
        [KeyboardButton(text="Закон Ома")],
        [KeyboardButton(text="ЭДС источника тока")],
        [KeyboardButton(text="Последовательное соединение проводников")],
        [KeyboardButton(text="Параллельное соединение проводников")],
        [KeyboardButton(text="Работа электрического тока")],
        [KeyboardButton(text="Закон Джоуля-Ленца")],
        [KeyboardButton(text="Мощность тока")],
        [KeyboardButton(text="Первое правило Кирхгофа")],
        [KeyboardButton(text="Второе правило Кирхгофа")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)