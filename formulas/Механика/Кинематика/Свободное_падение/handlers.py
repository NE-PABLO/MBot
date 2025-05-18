import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями

# --------------------- Формулы свободного падения -----------------завершено
async def send_svobodnoe_padenie_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Кинематика",
            "Свободное падение",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Свободное падение тела по вертикали")
async def send_svobodnoe_padenie_po_vertikali_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Свободное_падение_тела_по_вертикали.jpg",
                              "Формула свободного падения тела по вертикали")

@router.message(F.text == "Движение тела по вертикали вниз")
async def send_dvizhenie_tela_vniz_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Движение_тела_по_вертикали_вниз.jpg",
                              "Формула движения тела по вертикали вниз")

@router.message(F.text == "Движение тела по вертикали вверх")
async def send_dvizhenie_tela_vverh_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Движение_тела_по_вертикали_вверх.jpg",
                              "Формула движения тела по вертикали вверх")
    
@router.message(F.text == "Проекции скорости при движении тела, брошенного под углом к горизонту")
async def send_proekzii_skorosti_broshennoe_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Проекции_скорости_при_движении_тела_брошенного_под_углом_к_горизонту.jpg",
                              "Формула проекции скорости при движении тела, брошенного под углом к горизонту")
    
@router.message(F.text == "Уравнения координат при движении тела, брошенного под углом к горизонту")
async def send_uravnenia_koordinat_broshennoe_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Уравнения_координат_при_движении_тела_брошенного_под_углом_к_горизонту.jpg",
                              "Формула уравнения координат при движении тела, брошенного под углом к горизонту")
    
@router.message(F.text == "Время полета при движении тела, брошенного под углом к горизонту")
async def send_vremya_poleta_broshennoe_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Время_полета_при_движении_тела_брошенного_под_углом_к_горизонту.jpg",
                              "Формула времени полета при движении тела, брошенного под углом к горизонту")
    
@router.message(F.text == "Дальность полета при движении тела, брошенного под углом к горизонту")
async def send_dalnost_poleta_broshennoe_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Дальность_полета_при_движении_тела_брошенного_под_углом_к_горизонту.jpg",
                              "Формула дальности полета при движении тела, брошенного под углом к горизонту")
    
@router.message(F.text == "Максимальная высота подъёма при движении тела, брошенного под углом к горизонту")
async def send_max_vysota_broshennoe_handler(message: Message):
    await send_svobodnoe_padenie_formula(message,
                              "Максимальная_высота_подъёма_при_движении_тела_брошенного_под_углом_к_горизонту.jpg",
                              "Формула максимальной высоты подъема при движении тела, брошенного под углом к горизонту")
   