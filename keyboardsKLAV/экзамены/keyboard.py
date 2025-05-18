import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Базовый путь к директориям с темами кодификатора ЕГЭ
# Важно: этот путь должен быть доступен из окружения, где исполняется бот.
# Для локального тестирования или если структура фиксирована, можно захардкодить.
# В реальном боте лучше передавать через конфигурацию.
EXAMS_FORMULA_BASE_PATH = "/home/ubuntu/twoversion_extracted/twoversion/экзамены/егэ/Кодификатор2025"

def get_exams_type_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="ЕГЭ"), KeyboardButton(text="ОГЭ")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ege_options_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Кодификатор ЕГЭ")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ege_codificator_physics_sections_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Механика (ЕГЭ Кодификатор)")],
        [KeyboardButton(text="Молекулярная физика (ЕГЭ Кодификатор)")],
        [KeyboardButton(text="Термодинамика (ЕГЭ Кодификатор)")],
        [KeyboardButton(text="Электродинамика (ЕГЭ Кодификатор)")],
        # TODO: Добавить другие разделы, если они есть в структуре папок (Квантовая, СТО и т.д.)
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Клавиатуры для тем внутри разделов физики (Кодификатор ЕГЭ) ---

def get_ege_codificator_mechanics_topics_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Кинематика (ЕГЭ Механика)")],
        [KeyboardButton(text="Динамика (ЕГЭ Механика)")],
        [KeyboardButton(text="Статика (ЕГЭ Механика)")],
        [KeyboardButton(text="Законы сохранения в механике (ЕГЭ Механика)")],
        [KeyboardButton(text="Механические колебания и волны (ЕГЭ Механика)")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ege_codificator_molecular_physics_topics_keyboard() -> ReplyKeyboardMarkup:
    # Пример, нужно будет актуализировать согласно папкам
    buttons = [
        [KeyboardButton(text="Основные положения МКТ (ЕГЭ Молекулярная)")],
        [KeyboardButton(text="Идеальный газ (ЕГЭ Молекулярная)")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ege_codificator_thermodynamics_topics_keyboard() -> ReplyKeyboardMarkup:
    # Пример, нужно будет актуализировать согласно папкам
    buttons = [
        [KeyboardButton(text="Внутренняя энергия (ЕГЭ Термодинамика)")],
        [KeyboardButton(text="Работа в термодинамике (ЕГЭ Термодинамика)")],
        [KeyboardButton(text="Первый закон термодинамики (ЕГЭ Термодинамика)")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ege_codificator_electrodynamics_topics_keyboard() -> ReplyKeyboardMarkup:
    # Пример, нужно будет актуализировать согласно папкам
    buttons = [
        [KeyboardButton(text="Электростатика (ЕГЭ Электродинамика)")],
        [KeyboardButton(text="Постоянный ток (ЕГЭ Электродинамика)")],
        [KeyboardButton(text="Магнитное поле (ЕГЭ Электродинамика)")],
        [KeyboardButton(text="Электромагнитная индукция (ЕГЭ Электродинамика)")],
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Динамическая генерация клавиатур для формул --- 

def create_formula_keyboard_from_path(topic_folder_path: str) -> ReplyKeyboardMarkup | None:
    buttons = []
    try:
        if not os.path.isdir(topic_folder_path):
            print(f"Error: Directory not found for formulas: {topic_folder_path}")
            return None # Или вернуть клавиатуру с сообщением об ошибке
        
        # Ищем файлы .py, предполагая, что для каждого есть .jpg или .png
        formula_files = [f for f in os.listdir(topic_folder_path) if os.path.isfile(os.path.join(topic_folder_path, f)) and f.endswith(".py")]
        
        if not formula_files:
            # Можно добавить кнопку "Формулы для этого раздела еще не добавлены"
            buttons.append([KeyboardButton(text="Формулы не найдены")])

        for formula_file in sorted(formula_files):
            formula_name = os.path.splitext(formula_file)[0] # Убираем .py
            # Текст кнопки - это имя формулы. Пользователь сказал "нажму и у меня отправится фото"
            buttons.append([KeyboardButton(text=formula_name)])
            
    except Exception as e:
        print(f"Error creating formula keyboard for {topic_folder_path}: {e}")
        # Можно вернуть клавиатуру с сообщением об ошибке
        buttons.append([KeyboardButton(text="Ошибка загрузки списка формул")])

    buttons.append([KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, row_width=1) # row_width=1 для длинных названий формул

# --- Конкретные клавиатуры для формул по темам (используют create_formula_keyboard_from_path) ---

# Механика
def get_ege_mechanics_kinematics_formulas_keyboard() -> ReplyKeyboardMarkup:
    path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МЕХАНИКА", "КИНЕМАТИКА")
    return create_formula_keyboard_from_path(path)

def get_ege_mechanics_dynamics_formulas_keyboard() -> ReplyKeyboardMarkup:
    path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МЕХАНИКА", "ДИНАМИКА")
    return create_formula_keyboard_from_path(path)

def get_ege_mechanics_statics_formulas_keyboard() -> ReplyKeyboardMarkup:
    path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МЕХАНИКА", "СТАТИКА И ГИДРОСТАТИКА") # Папка может называться иначе
    return create_formula_keyboard_from_path(path)

def get_ege_mechanics_conservation_laws_formulas_keyboard() -> ReplyKeyboardMarkup:
    path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МЕХАНИКА", "ЗАКОНЫ СОХРАНЕНИЯ В МЕХАНИКЕ")
    return create_formula_keyboard_from_path(path)

def get_ege_mechanics_oscillations_formulas_keyboard() -> ReplyKeyboardMarkup:
    path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МЕХАНИКА", "МЕХАНИЧЕСКИЕ КОЛЕБАНИЯ И ВОЛНЫ")
    return create_formula_keyboard_from_path(path)

# TODO: Добавить аналогичные функции для Молекулярной физики, Термодинамики, Электродинамики
# Например:
# def get_ege_molecular_mkt_formulas_keyboard() -> ReplyKeyboardMarkup:
#     path = os.path.join(EXAMS_FORMULA_BASE_PATH, "МОЛЕКУЛЯРНАЯ ФИЗИКА", "ОСНОВНЫЕ ПОЛОЖЕНИЯ МКТ")
#     return create_formula_keyboard_from_path(path)


