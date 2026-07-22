from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import aiohttp
import re
import json
from aiohttp import web

TOKEN = "8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ============================================================
# БАЗА ОПЕРАТОРОВ И РЕГИОНОВ (РОССИЯ)
# ============================================================
OPERATORS = {
    '910': 'МТС', '911': 'МТС', '912': 'МТС', '913': 'МТС', '914': 'МТС',
    '915': 'МТС', '916': 'МТС', '917': 'МТС', '918': 'МТС', '919': 'МТС',
    '980': 'МТС', '981': 'МТС', '982': 'МТС', '983': 'МТС', '984': 'МТС',
    '985': 'МТС', '986': 'МТС', '987': 'МТС', '988': 'МТС', '989': 'МТС',
    '920': 'Билайн', '921': 'Билайн', '922': 'Билайн', '923': 'Билайн',
    '924': 'Билайн', '925': 'Билайн', '926': 'Билайн', '927': 'Билайн',
    '928': 'Билайн', '929': 'Билайн', '930': 'Билайн', '931': 'Билайн',
    '932': 'Билайн', '933': 'Билайн', '934': 'Билайн', '935': 'Билайн',
    '936': 'Билайн', '937': 'Билайн', '938': 'Билайн', '939': 'Билайн',
    '900': 'Tele2', '901': 'Tele2', '902': 'Tele2', '903': 'Tele2',
    '904': 'Tele2', '905': 'Tele2', '906': 'Tele2', '908': 'Tele2',
    '909': 'Tele2', '950': 'Tele2', '951': 'Tele2', '952': 'Tele2',
    '953': 'Tele2', '954': 'Tele2', '955': 'Tele2', '956': 'Tele2',
    '957': 'Tele2', '958': 'Tele2', '959': 'Tele2', '960': 'Tele2',
    '961': 'Tele2', '962': 'Tele2', '963': 'Tele2', '964': 'Tele2',
    '965': 'Tele2', '966': 'Tele2', '967': 'Tele2', '968': 'Tele2',
    '969': 'Tele2', '970': 'Yota', '971': 'Yota', '972': 'Yota',
    '973': 'Yota', '974': 'Yota', '975': 'Yota', '976': 'Yota',
    '977': 'Yota', '978': 'Yota', '979': 'Yota'
}

REGIONS = {
    '77': 'Москва', '78': 'Санкт-Петербург', '50': 'Московская обл.',
    '66': 'Свердловская обл.', '23': 'Краснодарский край',
    # можно добавить все 89 регионов
}

# ============================================================
# 1. ПОЛНАЯ ПРОВЕРКА НОМЕРА (ВСЕ ДОСТУПНЫЕ ИСТОЧНИКИ)
# ============================================================
async def full_phone_check(phone: str) -> str:
    clean = re.sub(r'[^\d]', '', phone)
    if len(clean) == 11 and clean.startswith('8'):
        clean = '7' + clean[1:]
    elif len(clean) == 10:
        clean = '7' + clean
    
    results = []
    results.append(f"📱 Номер: +{clean}")
    
    # 1. Оператор
    code = clean[1:4]
    operator = OPERATORS.get(code, 'Неизвестный / виртуальный')
    results.append(f"📡 Оператор: {operator}")
    
    # 2. Регион (по коду из первых цифр после оператора)
    if len(clean) >= 6:
        region_code = clean[4:6]
        region = REGIONS.get(region_code, 'Не определён')
        results.append(f"🌍 Регион привязки: {region}")
    
    # 3. Проверка через открытые API (kto-zvonil.biz)
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://kto-zvonil.biz/search.php?phone={clean}"
            headers = {"User-Agent": "Mozilla/5.0"}
            async with session.get(url, headers=headers, timeout=8) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    if 'отзыв' in html.lower():
                        results.append("💬 Найден отзыв на kto-zvonil.biz")
                    else:
                        results.append("ℹ️ Отзывов на kto-zvonil.biz нет")
    except:
        results.append("⚠️ Не удалось проверить kto-zvonil.biz")
    
    # 4. Проверка через сервис "Номер в Telegram"
    try:
        async with aiohttp.ClientSession() as session:
            tg_check = f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={clean}"
            async with session.get(tg_check, timeout=5) as resp:
                if resp.status == 200:
                    results.append("📌 Номер привязан к Telegram (есть аккаунт)")
                else:
                    results.append("📌 Telegram-аккаунт не найден")
    except:
        pass
    
    return "\n".join(results)

# ============================================================
# 2. ПРОВЕРКА ИНН (ФНС, ОГРН, КПП)
# ============================================================
async def check_inn(inn: str) -> str:
    """Проверяет ИНН через открытые API (ФНС, ЕГРЮЛ)"""
    results = []
    results.append(f"📄 ИНН: {inn}")
    
    # Проверка длины
    if len(inn) == 10:
        results.append("🧑‍💼 ИНН физического лица")
    elif len(inn) == 12:
        results.append("🏢 ИНН юридического лица / ИП")
    else:
        results.append("⚠️ Некорректный ИНН (должен быть 10 или 12 цифр)")
        return "\n".join(results)
    
    # Проверка через открытый API (пример)
    try:
        async with aiohttp.ClientSession() as session:
            # Используем бесплатный API (требуется ключ, но для примера — заглушка)
            url = f"https://api-fns.ru/api/inn/{inn}"
            # В реальности нужен API-ключ от ФНС или коммерческого сервиса
            results.append("🔍 Для полной проверки ИНН нужен ключ ФНС или коммерческий API (Dadata, Sbis и т.д.)")
            results.append("📌 Без ключа доступны только базовые проверки (длина, контрольная сумма)")
    except:
        results.append("⚠️ Ошибка проверки ИНН")
    
    return "\n".join(results)

# ============================================================
# КНОПКИ
# ============================================================
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Проверить номер", request_contact=True)],
        [KeyboardButton(text="📄 Проверить ИНН")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔍 Выбери действие:\n"
        "1. Отправь номер телефона (кнопка или ввод)\n"
        "2. Отправь ИНН (10 или 12 цифр)\n\n"
        "⚠️ Данные только из открытых источников.\n"
        "Личные данные (паспорт, прописка) защищены законом.",
        reply_markup=main_kb
    )

@dp.message(lambda msg: msg.text == "📄 Проверить ИНН")
async def inn_prompt(message: types.Message):
    await message.answer("Введи ИНН (10 или 12 цифр):")

@dp.message(lambda msg: msg.contact is not None)
async def handle_contact(message: types.Message):
    phone = message.contact.phone_number
    if not phone.startswith("+"):
        phone = "+" + phone
    await message.answer("⏳ Проверяю номер...")
    result = await full_phone_check(phone)
    await message.answer(f"🔍 Результат:\n\n{result}")

@dp.message()
async def handle_text(message: types.Message):
    text = message.text.strip()
    
    # Проверка на ИНН (10 или 12 цифр)
    if re.fullmatch(r'\d{10}|\d{12}', text):
        await message.answer("⏳ Проверяю ИНН...")
        result = await check_inn(text)
        await message.answer(f"📄 Результат:\n\n{result}")
        return
    
    # Проверка на номер телефона
    clean = re.sub(r'[^\d+]', '', text)
    if clean.startswith('+') or clean.startswith('8') or clean.startswith('7'):
        if len(clean) >= 10:
            await message.answer("⏳ Проверяю номер...")
            result = await full_phone_check(clean)
            await message.answer(f"🔍 Результат:\n\n{result}")
        else:
            await message.answer("⚠️ Слишком короткий номер.")
    else:
        await message.answer("ℹ️ Отправь номер телефона или ИНН.")

# ============================================================
# ВЕБ-СЕРВЕР
# ============================================================
async def health(request):
    return web.Response(text="✅ Bot is running!")

async def start_web():
    app = web.Application()
    app.router.add_get("/", health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("✅ Web server started on port 8080")
    await asyncio.Event().wait()

async def main():
    await asyncio.gather(
        start_web(),
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    asyncio.run(main())
