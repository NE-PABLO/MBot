from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Электродинамика_Магнитное поле и электромагнитная индукция ---------------
def get_magnetic_field_and_electromagnetic_induction_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Линии магнитной индукции")],
        [KeyboardButton(text="Графическое представление магнитного поля")],
        [KeyboardButton(text="Правило правой руки или правило буравчика")],
        [KeyboardButton(text="Сила Ампера")],
        [KeyboardButton(text="Правило левой руки")],
        [KeyboardButton(text="Сила Лоренца")],
        [KeyboardButton(text="Явление электромагнитной индукции")],
        [KeyboardButton(text="Поток вектора магнитной индукции")],
        [KeyboardButton(text="Закон электромагнитной индукции Фарадея")],
        [KeyboardButton(text="ЭДС индукции в прямом проводнике, движущемся в магнитном поле")],
        [KeyboardButton(text="Индуктивность")],
        [KeyboardButton(text="ЭДС самоиндукции")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)