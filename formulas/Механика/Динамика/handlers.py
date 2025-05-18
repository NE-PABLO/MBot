import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы динамики -----------------завершено
async def send_dynamics_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Динамика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Плотность вещества")
async def plotnost_veshestva_handler(message: Message):
    await send_dynamics_formula(message,
                              "Плотность_вещества.jpg",
                              "Формула плотности вещетсва")

@router.message(F.text == "Равнодействующая сил")
async def ravnodeistvuyushaya_handler(message: Message):
    await send_dynamics_formula(message,
                              "Равнодействующая_сил.jpg",
                              "Формула равнодействующей силы")

@router.message(F.text == "Первый закон Ньютона")
async def newton_first_handler(message: Message):
    await send_dynamics_formula(message,
                              "Первый_закон_Ньютона.jpg",
                              "Первый закон Ньютона")

@router.message(F.text == "Второй закон Ньютона")
async def newton_second_handler(message: Message):
    await send_dynamics_formula(message,
                              "Второй_закон_Ньютона.jpg",
                              "Второй закон Ньютона: F = ma")

@router.message(F.text == "Третий закон Ньютона")
async def newton_third_handler(message: Message):
    await send_dynamics_formula(message,
                              "Третий_закон_Ньютона.jpg",
                              "Третий закон Ньютона")

@router.message(F.text == "Сила трения")
async def sila_treniya_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_трения.jpg",
                              "Формула силы трения")

@router.message(F.text == "Сила упругости")
async def sila_uprugosti_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_упругости.jpg",
                              "Закон Гука: F = -kx")

@router.message(F.text == "Закон всемирного тяготения")
async def gravitation_handler(message: Message):
    await send_dynamics_formula(message,
                              "Закон_всемирного_тяготения.jpg",
                              "Закон всемирного тяготения Ньютона")

@router.message(F.text == "Сила тяжести")
async def sila_tyazhesti_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_тяжести.jpg",
                              "Формула силы тяжести")

@router.message(F.text == "Сила нормального давления, если тело покоится (движется равномерно)")
async def sila_normalnaya_pokoi_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_нормального_давления_если_тело_покоится.jpg",
                              "Сила нормальной реакции опоры")

@router.message(F.text == "Сила нормального давления, если телодвижется с ускорением, направленным вверх")
async def sila_normalnaya_vverh_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_нормального_давления_если_тело_движется_с_ускорением_направленным_вверх.jpg",
                              "Сила реакции опоры при ускорении вверх")

@router.message(F.text == "Сила нормального давления, если телодвижется с ускорением, направленным вниз")
async def sila_normalnaya_vniz_handler(message: Message):
    await send_dynamics_formula(message,
                              "Сила_нормального_давления_если_тело_движется_с_ускорением_направленным_вниз.jpg",
                              "Сила реакции опоры при ускорении вниз")

@router.message(F.text == "Вес тела")
async def ves_tela_handler(message: Message):
    await send_dynamics_formula(message,
                              "Вес_тела.jpg",
                              "Формула веса тела")

@router.message(F.text == "Первая космическая скорость")
async def pervaya_kosmicheskaya_handler(message: Message):
    await send_dynamics_formula(message,
                              "Первая_космическая_скорость.jpg",
                              "Первая космическая скорость")

@router.message(F.text == "Вторая космическая скорость")
async def vtoraya_kosmicheskaya_handler(message: Message):
    await send_dynamics_formula(message,
                              "Вторая_космическая_скорость.jpg",
                              "Вторая космическая скорость")
