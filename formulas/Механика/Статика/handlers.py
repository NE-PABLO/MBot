import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

router = Router()

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 



# --------------------- Формулы Статики -----------------
async def send_statika_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Статика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Момент силы")
async def moment_sili_handler(message: Message):
    await send_statika_formula(message,
                              "Момент_силы.jpg",
                              "Формула момента силы")
    
@router.message(F.text == "Условие равновесия рычага")
async def uslovie_ravnovesiya_rychaga_handler(message: Message):
    await send_statika_formula(message,
                              "Условие_равновесия_рычага.jpg",
                              "Формула условия равновесия рычага")
    
@router.message(F.text == "Условия равновесия твердого тела в ИСО")
async def usloviya_ravnovesiya_tverdogo_tela_v_ISO_handler(message: Message):
    await send_statika_formula(message,
                              "Условия_равновесия_твердого_тела_в_ИСО.jpg",
                              "Формула условий равновесия твердого тела в ИСО")
    
@router.message(F.text == "Неподвижный блок")
async def nepodvizhniy_block_handler(message: Message):
    await send_statika_formula(message,
                              "Неподвижный_блок.jpg",
                              "Формула неподвижного блока")
    
@router.message(F.text == "Подвижный блок")
async def podvizhniy_block_handler(message: Message):
    await send_statika_formula(message,
                              "Подвижный_блок.jpg",
                              "Формула подвижного блока")
    
@router.message(F.text == "Коэффициент полезного действия или КПД")
async def kpd_handler(message: Message):
    await send_statika_formula(message,
                              "Коэффициент_полезного_действия_или_КПД.jpg",
                              "Формула коэффициента полезного действия или КПД")
    
@router.message(F.text == "Гидростатическое давление")
async def gidrostaticheskoe_davlenie_handler(message: Message):
    await send_statika_formula(message,
                              "Гидростатическое_давление.jpg",
                              "Формула гидростатического давления")
    
@router.message(F.text == "Закон Паскаля")
async def zakon_paskalya_handler(message: Message):
    await send_statika_formula(message,
                              "Закон_Паскаля.jpg",
                              "Закон Паскаля")
    
@router.message(F.text == "Закон Архимеда")
async def zakon_arhimeda_handler(message: Message):
    await send_statika_formula(message,
                              "Закон_Архимеда.jpg",
                              "Закон Архимеда")
    
@router.message(F.text == "Условие плавания тел")
async def uslovie_plavaniya_tel_handler(message: Message):
    await send_statika_formula(message,
                              "Условие_плавания_тел.jpg",
                              "Формула условия плавания тел")