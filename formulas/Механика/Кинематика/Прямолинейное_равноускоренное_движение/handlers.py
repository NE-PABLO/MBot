import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 


# --------- Прямолинейное равноускоренное движение -----------завершено
async def send_ravn_yskoren_dvizh_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Кинематика",
            "Прямолинейное_равноускоренное_движение",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Ускорение при равноускоренном прямолинейном движении")
async def send_uskorenie_ravn_pram_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "Ускорение_при_равноускоренном_прямолинейном_движении.jpg",
                              "Формула скорости прямолинейного равномерного движения")

@router.message(F.text == "Скорость при равноускоренном прямолинейном движении")
async def send_skorost_ravnoyskoren_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "Скорость_при_равноускоренном_прямолинейном_движении.jpg",
                              "Формула скорости при равноускоренном прямолинейном движении")

@router.message(F.text == "Проекция перемещения при равноускоренном прямолинейном движении")
async def send_proekzia_peremeshenie_ravnoysk_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "Проекция_перемещения_при_равноускоренном_прямолинейном_движении.jpg",
                              "Проекция перемещения при равноускоренном прямолинейном движении")

@router.message(F.text == "Зависимость координаты от времени при равноускоренном прямолинейном движении")
async def send_zavisimost_kordinata_ravnoyskorenoe_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "Зависимость_координаты_от_времени_при_равноускоренном_прямолинейном_движении.jpg",
                              "Зависимость координаты от времени при равноускоренном прямолинейном движении")

@router.message(F.text == "График зависимости проекции ускорения от времени при равноускоренном прямолинейном движении")
async def send_graf_zavist_proekz_yskor_ravnyskor_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "График_зависимости_проекции_ускорения_от_времени .jpg",
                              "График зависимости проекции ускорения от времени при равноускоренном прямолинейном движении")

@router.message(F.text == "График зависимости проекции скорости от времени при равноускоренном прямолинейном движении")
async def send_graf_zav_proekz_skorost_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "График_зависимости_проекции_скорости_от_времени_при_равноускоренном_прямолинейном_движении.jpg",
                              "График зависимости проекции скорости от времени при равноускоренном прямолинейном движении")

@router.message(F.text == "График зависимости координаты от времени при равноускоренном прямолинейном движении")
async def send_graf_zavist_kordinata_ravnyskor_handler(message: Message):
    await send_ravn_yskoren_dvizh_formula(message,
                              "График_зависимости_координаты_от_времени_при_равноускоренном_прямолинейном_движении.jpg",
                              "График зависимости координаты от времени при равноускоренном прямолинейном движении")