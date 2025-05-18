from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Раздел: Электродинамика_Электрическое поле ---------------
def get_electric_field_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Закон Кулона")],
        [KeyboardButton(text="Напряженность электрического поля")],
        [KeyboardButton(text="Напряженность поля точечного заряда")],
        [KeyboardButton(text="Потенциал точки электростатического поля")],
        [KeyboardButton(text="Разность потенциалов (напряжение)")],
        [KeyboardButton(text="Электроёмкость")],
        [KeyboardButton(text="Соединение конденсаторов (параллельное/последовательное)")],
        [KeyboardButton(text="Энергия заряженного конденсатора")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)