from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Законы сохранения в механике -----------------
def get_zakony_sohraneniya_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Импульс")],
        [KeyboardButton(text="Второй закон Ньютона в импульсной форме")],
        [KeyboardButton(text="Закон сохранения импульса")],
        [KeyboardButton(text="Закон сохранения импульса при абсолютно упругом ударе")],
        [KeyboardButton(text="Закон сохранения импульса при абсолютно неупругом ударе")],
        [KeyboardButton(text="Реактивное движение")],
        [KeyboardButton(text="Механическая работа")],
        [KeyboardButton(text="Мощность")],
        [KeyboardButton(text="Кинетическая энергия")],
        [KeyboardButton(text="Потенциальная энергия тела, поднятого над Землей")],
        [KeyboardButton(text="Потенциальная энергия упруго деформированного тела")],
        [KeyboardButton(text="Теорема об изменении кинетической энергии")],
        [KeyboardButton(text="Полная механическая энергия")],
        [KeyboardButton(text="Закон сохранения механической энергии")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)