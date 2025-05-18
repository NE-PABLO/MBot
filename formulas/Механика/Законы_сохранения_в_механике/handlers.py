import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы законов сохранения в механике -----------------
async def send_zakony_sohraneniya_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Законы сохранения в механике",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Импульс")
async def impulsa_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Импульс.jpg",
                              "Формула импульса")
    
@router.message(F.text == "Второй закон Ньютона в импульсной форме")
async def newton_second_impuls_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Второй_закон_Ньютона_в_импульсной_форме.jpg",
                              "Второй закон Ньютона в импульсной форме")
    
@router.message(F.text == "Закон сохранения импульса")
async def zakon_sohraneniya_impulsa_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Закон_сохранения_импульса.jpg",
                              "Закон сохранения импульса")
    
@router.message(F.text == "Закон сохранения импульса при абсолютно упругом ударе")
async def zakon_sohraneniya_impulsa_uprugiy_udar_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Закон_сохранения_импульса_при_абсолютно_упругом_ударе.jpg",
                              "Закон сохранения импульса при абсолютно упругом ударе")
    
@router.message(F.text == "Закон сохранения импульса при абсолютно неупругом ударе")
async def zakon_sohraneniya_impulsa_neuprugiy_udar_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Закон_сохранения_импульса_при_абсолютно_неупругом_ударе.jpg",
                              "Закон сохранения импульса при абсолютно неупругом ударе")
    
@router.message(F.text == "Реактивное движение")
async def reaktivnoe_dvizhenie_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Реактивное_движение.jpg",
                              "Формула реактивного движения")
    
@router.message(F.text == "Механическая работа")
async def mehanicheskaya_rabota_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Механическая_работа.jpg",
                                "Формула механической работы")
    
@router.message(F.text == "Мощность")
async def moshnost_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Мощность.jpg",
                              "Формула мощности")
    
@router.message(F.text == "Кинетическая энергия")
async def kineticheskaya_energiya_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Кинетическая_энергия.jpg",
                              "Формула кинетической энергии")
    
@router.message(F.text == "Потенциальная энергия тела, поднятого над Землей")
async def potencialnaya_energiya_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Потенциальная_энергия_тела,_поднятого_над_Землей.jpg",
                              "Формула потенциальной энергии тела, поднятого над Землей")
    
@router.message(F.text == "Потенциальная энергия упруго деформированного тела")
async def potencialnaya_energiya_uprugiy_deformirovanniy_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Потенциальная_энергия_упруго_деформированного_тела.jpg",
                              "Формула потенциальной энергии упруго деформированного тела")
    
@router.message(F.text == "Теорема об изменении кинетической энергии")
async def teorema_ob_izmenenii_kineticheskoy_energii_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Теорема_об_изменении_кинетической_энергии.jpg",
                              "Теорема об изменении кинетической энергии")
    
@router.message(F.text == "Полная механическая энергия")
async def polnaya_mehanicheskaya_energiya_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Полная_механическая_энергия.jpg",
                              "Формула полной механической энергии")
    
@router.message(F.text == "Закон сохранения механической энергии")
async def zakon_sohraneniya_mehanicheskoy_energii_handler(message: Message):
    await send_zakony_sohraneniya_formula(message,
                              "Закон_сохранения_механической_энергии.jpg",
                              "Закон сохранения механической энергии")