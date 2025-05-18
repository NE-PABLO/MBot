from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Ядерная физика ---------------
def get_nuclear_physics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Массовое число")],
        [KeyboardButton(text="Спектр уровней энергии атома водорода")],
        [KeyboardButton(text="Планетарная модель атома")],
        [KeyboardButton(text="Состав атома")],
        [KeyboardButton(text="Энергия связи")],
        [KeyboardButton(text="Изотопы")],
        [KeyboardButton(text="Альфа и бета распад")],
        [KeyboardButton(text="Обозначение атомного ядра")],
        [KeyboardButton(text="Дефект массы ядра")],
        [KeyboardButton(text="Закон радиоактивного распада")],
        [KeyboardButton(text="Масса фотона")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)