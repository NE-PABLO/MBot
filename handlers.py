"""# Импорт необходимых библиотек и модулей
import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import *
from difflib import get_close_matches

# Импорт конфигурации и состояний
from config import BASE_IMAGE_PATH
from states import user_states, previous_states, state_keyboards, user_state_stack, SEARCH_KEYWORDS

# Создание маршрутизатора для обработки сообщений
router = Router()

# Импорт клавиатур для различных разделов
from keyboardsKLAV import *

# Импорт комментариев
import keyboardsKOMMENT.komment as kb

from formulas import *

from fuzzywuzzy import process, fuzz

# ========================================================
# ОБРАБОТЧИКИ КОМАНД И СООБЩЕНИЙ
# ========================================================

# --------------------- Системные команды ----------------

# Обработчик команды поиска
@router.message(Command("poisk"))
@router.message(F.text.casefold() == "поиск")
async def start_search(message: Message):
    user_id = message.from_user.id
    update_user_state(user_id, 'search') # Используем update_user_state для консистентности
    await message.answer("🔍 Введите название формулы или раздела для поиска:")

# Обработчик команды /start
@router.message(Command("start"))
async def start(message: Message):
    print("Обработчик start вызван!")
    user_id = message.from_user.id
    user_state_stack[user_id] = ['main']
    user_states[user_id] = 'main'
    await message.answer(
        "Добро пожаловать! Выберите раздел физики:",
        reply_markup=get_main_keyboard()
    )

# Функция для обновления состояния пользователя
def update_user_state(user_id, new_state):
    if user_id not in user_state_stack:
        user_state_stack[user_id] = ['main'] # Инициализируем с main, если стека нет
    
    current_stack = user_state_stack[user_id]
    if not current_stack or current_stack[-1] != new_state:
        current_stack.append(new_state)
    
    user_states[user_id] = new_state

# Обработчик для кнопки "Назад"
@router.message(F.text == "Назад")
async def back_button_handler(message: Message):
    user_id = message.from_user.id
    current_stack = user_state_stack.get(user_id, [])
    
    if len(current_stack) > 1:
        current_stack.pop()
        previous_actual_state = current_stack[-1]
        user_states[user_id] = previous_actual_state
    else:
        user_states[user_id] = 'main'
        user_state_stack[user_id] = ['main']

    current_state_for_keyboard = user_states[user_id]
    
    if current_state_for_keyboard in state_keyboards:
        keyboard_func = state_keyboards[current_state_for_keyboard]
        reply_text = f"Возвращаемся..."
        if current_state_for_keyboard == 'main':
            reply_text = "Возвращаемся в главное меню:"
        else:
            # Более осмысленный текст для кнопки "Назад"
            # Можно использовать словарь для маппинга состояний в названия разделов
            state_to_title = {
                'exams_type_selection': "Выбор типа экзамена",
                'ege_options': "ЕГЭ",
                'ege_codificator_physics_sections': "Разделы физики (Кодификатор ЕГЭ)",
                'ege_codificator_mechanics_topics': "Темы по Механике (Кодификатор ЕГЭ)",
                # ... другие состояния
            }
            reply_text = state_to_title.get(current_state_for_keyboard, f"Вы вернулись в раздел: {current_state_for_keyboard}")
        await message.answer(reply_text, reply_markup=keyboard_func())
    else:
        user_states[user_id] = 'main'
        user_state_stack[user_id] = ['main']
        await message.answer(
            "Не удалось определить предыдущее меню, возвращаемся в главное.",
            reply_markup=get_main_keyboard()
        )

# Обработчик для возврата в главное меню
@router.message(F.text == "Главное меню")
async def main_menu_handler(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = 'main'
    user_state_stack[user_id] = ['main']
    await message.answer(
        "Возвращаемся в главное меню:",
        reply_markup=get_main_keyboard()
    )

# Универсальная функция для обработки сообщений с текстом и состоянием
async def handle_message_with_state(message: Message, state: str, reply_text: str, keyboard_func):
    user_id = message.from_user.id
    update_user_state(user_id, state)
    await message.answer(reply_text, reply_markup=keyboard_func())

# Универсальная функция для отправки изображений
async def send_image_formula(message: Message, folder: str, filename: str, caption: str):
    try:
        # Путь к изображениям для формул экзаменов может отличаться, нужно будет уточнить
        # Например, /home/ubuntu/twoversion_extracted/twoversion/экзамены/егэ/Кодификатор2025/МЕХАНИКА/КИНЕМАТИКА/filename.py (тут .py, а не .jpg)
        # Пользователь сказал "фото сам добавлю", но структура папок указывает на .py файлы с кодом, а не картинки.
        # Пока оставим как есть, но это место для уточнения.
        image_path = os.path.join(BASE_IMAGE_PATH, folder, filename) # BASE_IMAGE_PATH может быть нерелевантен для экзаменов
        
        # Проверяем, существует ли файл перед отправкой
        # if not os.path.exists(image_path):
        #     # Альтернативный путь для экзаменов, если структура другая
        #     alt_image_path = os.path.join("/home/ubuntu/twoversion_extracted/twoversion/экзамены/егэ/Кодификатор2025", folder, filename)
        #     if os.path.exists(alt_image_path):
        #         image_path = alt_image_path
        #     else:
        #         await message.answer(f"⚠️ Изображение не найдено: {filename}")
        #         return

        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки изображения: {str(e)}")

# --- ОБРАБОТЧИКИ ДЛЯ РАЗДЕЛА "ЭКЗАМЕНЫ" ---
@router.message(F.text == "Экзамены")
async def exams_handler(message: Message):
    await handle_message_with_state(
        message,
        state="exams_type_selection",
        reply_text="Выберите тип экзамена:",
        keyboard_func=get_exams_type_keyboard
    )

@router.message(F.text == "ЕГЭ")
async def ege_handler(message: Message):
    await handle_message_with_state(
        message,
        state="ege_options",
        reply_text="Выберите опцию для ЕГЭ:",
        keyboard_func=get_ege_options_keyboard
    )

@router.message(F.text == "ОГЭ")
async def oge_handler(message: Message):
    # Логика для ОГЭ (пока не реализована, согласно ТЗ)
    await message.answer("Раздел ОГЭ пока в разработке.", reply_markup=get_exams_type_keyboard()) # Возврат на предыдущий шаг
    # update_user_state(message.from_user.id, 'exams_type_selection') # Явное обновление состояния

@router.message(F.text == "Кодификатор ЕГЭ")
async def ege_codificator_handler(message: Message):
    user_id = message.from_user.id
    update_user_state(user_id, "ege_codificator_physics_sections")
    
    # Отправка файла кодификатора
    codificator_file_path = "/home/ubuntu/twoversion_extracted/twoversion/экзамены/егэ/Кодификатор2025/Кодификатор2025.pdf" # Пример пути, нужно уточнить реальный путь и имя файла
    try:
        # Проверяем наличие файла
        if os.path.exists(codificator_file_path):
            document = FSInputFile(codificator_file_path)
            await message.answer_document(document, caption="Файл кодификатора ЕГЭ")
        else:
            await message.answer("Файл кодификатора не найден. Пожалуйста, проверьте путь к файлу.")
    except Exception as e:
        await message.answer(f"Ошибка при отправке файла кодификатора: {str(e)}")
    
    await message.answer(
        "Выберите раздел физики из кодификатора ЕГЭ:",
        reply_markup=get_ege_codificator_physics_sections_keyboard()
    )

# Обработчики для разделов физики в кодификаторе ЕГЭ
@router.message(F.text == "Механика (ЕГЭ Кодификатор)")
async def ege_codificator_mechanics_handler(message: Message):
    await handle_message_with_state(
        message,
        state="ege_codificator_mechanics_topics",
        reply_text="Выберите тему по механике (Кодификатор ЕГЭ):",
        keyboard_func=get_ege_codificator_mechanics_topics_keyboard
    )

# TODO: Добавить обработчики для других разделов физики (Молекулярная, Термодинамика, Электродинамика)
# по аналогии с ege_codificator_mechanics_handler

# --- КОНЕЦ ОБРАБОТЧИКОВ ДЛЯ РАЗДЕЛА "ЭКЗАМЕНЫ" ---


# --- СТАРЫЕ ОБРАБОТЧИКИ (ОСНОВНЫЕ РАЗДЕЛЫ ФИЗИКИ) ---
@router.message(F.text == "Механика")
async def mechanics_handler(message: Message):
    await handle_message_with_state(
        message,
        state="mechanics",
        reply_text="Раздел механики:",
        keyboard_func=get_mechanics_keyboard
    )

# ... (остальные существующие обработчики без изменений)
@router.message(F.text == "Количество вещества")
async def kolichestvo_veshestva_handler(message: Message):
    await send_image_formula(
        message,
        folder="Молекулярная физика",
        filename="Количество_вещества.jpg",
        caption="Понятие 'Количество вещества'"
    )

@router.message(F.text == "Кинематика")
async def kinematics_handler(message: Message):
    await handle_message_with_state(message, 'kinematics', "Раздел кинематики:", get_kinematics_keyboard)

@router.message(F.text == "Прямолинейное равномерное движение")
async def uniform_motion_handler(message: Message):
    await handle_message_with_state(message, 'uniform_motion', "Формулы прямолинейного равномерного движения:", get_ravnomernoe_keyboard)

@router.message(F.text == "Прямолинейное равноускоренное движение")
async def ravnoyskorenoe_handler(message: Message):
    await handle_message_with_state(message, 'ravnoyskorenoe', "Формулы прямолинейного равноускоренного движения:", get_ravnoyskorenoe_keyboard)

@router.message(F.text == "Свободное падение")
async def svobodnoe_padenie_handler(message: Message):
    await handle_message_with_state(message, 'svobodnoe_padenie', "Формулы свободного падения:", get_svobodnoe_padenie_keyboard)

@router.message(F.text == "Движение по окружности")
async def ravnomernoe_dvizhenie_po_okruzhnosti_handler(message: Message):
    await handle_message_with_state(message, 'ravnomernoe_dvizhenie_po_okruzhnosti', "Формулы равномерного движения по окружности:", get_ravnomernoe_dvizhenie_po_okruzhnosti_keyboard)

@router.message(F.text == "Динамика")
async def dinamika_handler(message: Message):
    await handle_message_with_state(message, 'dinamika', "Выберите формулу:", get_dinamika_keyboard)

@router.message(F.text == "Законы сохранения в механике")
async def zakony_sohraneniya_handler(message: Message):
    await handle_message_with_state(message, 'zakony_sohraneniya', "Формулы законов сохранения в механике:", get_zakony_sohraneniya_keyboard)

@router.message(F.text == "Статика")
async def statika_handler(message: Message):
    await handle_message_with_state(message, 'statika', "Формулы статики:", get_statika_keyboard)

@router.message(F.text == "Механические колебания и волны")
async def mech_kolebaniya_i_volny_handler(message: Message):
    await handle_message_with_state(message, 'mechanicheskie_kolebaniya_i_volny', "Формулы механических колебаний и волн:", get_mechanicheskie_kolebaniya_i_volny_keyboard)

@router.message(F.text == "Молекулярная физика")
async def molekylarn_handler(message: Message):
    user_id = message.from_user.id
    update_user_state(user_id, 'molekylarn')
    image_path = os.path.join(BASE_IMAGE_PATH, "Молекулярная физика", "Молекулярная_физика.jpg")
    try:
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption="Раздел молекулярной физики", reply_markup=get_molekylarn_keyboard())
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки изображения: {str(e)}")
        await message.answer("Раздел молекулярной физики:", reply_markup=get_molekylarn_keyboard())

@router.message(F.text == "Термодинамика")
async def thermodynamics_handler(message: Message):
    await handle_message_with_state(message, 'thermodynamics', "Раздел термодинамики:", get_thermodynamics_keyboard)

@router.message(F.text == "Электродинамика")
async def electrodynamics_handler(message: Message):
    await handle_message_with_state(message, 'electrodynamics', "Раздел электродинамики:", get_electrodynamics_keyboard)

@router.message(F.text == "Электрическое поле")
async def electric_field_handler(message: Message):
    await handle_message_with_state(message, 'electric_field', "Формулы электрического поля:", get_electric_field_keyboard)

@router.message(F.text == "Законы постоянного тока")
async def laws_of_constant_current_handler(message: Message):
    await handle_message_with_state(message, 'laws_of_constant_current', "Формулы законов постоянного тока:", get_zakon_postoinogo_toka_keyboard)

@router.message(F.text == "Магнитное поле и электромагнитная индукция")
async def magnetic_field_and_electromagnetic_induction_handler(message: Message):
    await handle_message_with_state(message, 'magnetic_field_and_electromagnetic_induction', "Формулы магнитного поля и электромагнитной индукции:", get_magnetic_field_and_electromagnetic_induction_keyboard)

@router.message(F.text == "Электромагнитные колебания и волны") 
async def electromagnetic_oscillations_and_waves_handler(message: Message):
    await handle_message_with_state(message, 'electromagnetic_oscillations_and_waves', "Формулы электромагнитных колебаний и волн:", get_electromagnetic_oscillations_and_waves_keyboard)

@router.message(F.text == "Оптика")
async def optics_handler(message: Message):
    await handle_message_with_state(message, 'optics', "Раздел оптики:", get_optics_keyboard)

@router.message(F.text == "Квантовая физика")
async def quantum_physics_handler(message: Message):
    await handle_message_with_state(message, 'quantum_physics', "Раздел квантовой физики:", get_quantum_physics_keyboard)

@router.message(F.text == "Ядерная физика")
async def nuclear_physics_handler(message: Message):
    await handle_message_with_state(message, 'nuclear_physics', "Раздел ядерной физики:", get_nuclear_physics_keyboard)

# Обработчик для комментариев и "Я не хочу" (оставлены как есть)
@router.message(F.text == "🎤 Ваш мега-коммент")
async def kommentarii_handler(message: Message):
    await message.reply("👀 Поймал баг? Придумал крутую фичу?\n"
    "🔥 Жги в комментариях — обсудим!\n\n"
    "💡 Топ-3 темы, которые нам интересны:\n"
    "1. \"Почему бот не...\" 🐛 — баги\n"
    "2. \"А сделайте так, чтобы...\" 🚀 — идеи\n"
    "3. \"Вообще огонь, но...\" 🔥 — отзывы\n\n"
    "📌 Пиши как есть: с матами (но в рамках), стикерами или даже голосовыми.\n\n"
    "▄︻デ══━💥  (っ◔◡◔)っ 🎮\n"
    "(бот не взорвётся от критики, проверено)",
    reply_markup=kb.main)

@router.message(F.text == "Я не хочу")
async def back_handler_ne_hochu(message: Message):
    await message.answer(
        "Хорошо, возвращаю назад!",
        reply_markup=kb.main  
    )

# Улучшенный обработчик поисковых запросов и неизвестных команд
@router.message(F.text)
async def handle_text_formula_or_search(message: Message):
    user_id = message.from_user.id
    text = message.text

    if user_states.get(user_id) == 'search':
        query = text.lower().strip()
        if not query:
            await message.answer("Пожалуйста, введите поисковый запрос.")
            return

        matches = process.extract(query, SEARCH_KEYWORDS, limit=5, scorer=fuzz.token_sort_ratio)
        matches = [match[0] for match in matches if match[1] > 50]

        if not matches:
            await message.answer("❌ Ничего не найдено. Попробуйте другой запрос.")
        else:
            buttons = [[KeyboardButton(text=match)] for match in matches]
            buttons.append([KeyboardButton(text="Главное меню")])
            await message.answer(
                "🔍 Результаты поиска:",
                reply_markup=ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
            )
        # После поиска возвращаем в состояние, откуда был вызван поиск, или в main
        # Это требует более сложной логики управления стеком для поиска
        # Пока просто возвращаем в main
        user_states[user_id] = 'main'
        user_state_stack[user_id] = ['main']
        return
    
    # Если текст не соответствует ни одной известной команде/кнопке
    # (кроме тех, что обрабатываются выше, как "Назад", "Главное меню" и т.д.)
    # Можно добавить сообщение о неизвестной команде или просто не реагировать.
    # await message.answer("Неизвестная команда. Пожалуйста, используйте кнопки меню.")

"""
