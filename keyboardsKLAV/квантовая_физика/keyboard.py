from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Квантовая физика ---------------
def get_quantum_physics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Формула Планка")],
        [KeyboardButton(text="Энергия фотона")],
        [KeyboardButton(text="Импульс фотона")],
        [KeyboardButton(text="Уравнение Эйнштейна для фотоэффекта")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)