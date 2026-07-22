from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import aiohttp
import json
from aiohttp import web

TOKEN = "8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== ФУНКЦИЯ ПОИСКА ПО НОМЕРУ (БЕСПЛАТНЫЕ ИСТОЧНИКИ) =====
async def search_phone(phone: str) -> str:
    results = []
    
    # 1. Проверка через бесплатный API (пример)
    try:
        async with aiohttp.ClientSession() as session:
            # Формируем номер в международном формате
            clean_phone = phone.replace("+", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            
            # Проверка через открытый API (пример)
            url = f"https://api.apilayer.com/number_verification/validate?number={clean_phone}"
            # Это заглушка — замени на реальный API ключ, если есть
            # results.append(f"📱 Оператор: ...")
            
            # 2. Проверка через открытые базы (заглушка)
            # В реальности нужно подключать платные API или парсить сайты
            results.append("🔍 Данные из открытых источников:")
            results.append("  - Регион: определяется по коду оператора")
            results.append("  - Оператор: MTS / Beeline / Tele2 и т.д.")
            results.append("  - Время: актуально на 2026 год")
            
            # 3. Проверка по утечкам (требуется API)
            results.append("⚠️ Для полноценного пробива нужен доступ к базам данных.")
            results.append("📌 Используй платные сервисы: LeakCheck, PhoneChecker, и т.д.")
    except Exception as e:
        results.append(f"⚠️ Ошибка: {str(e)}")
    
    return "\n".join(results)

# ===== КНОПКА =====
phone_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📱 Отправить номер", request_contact=True)]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔍 Введи номер телефона в формате +7XXXXXXXXXX\n"
        "Я попробую найти информацию по открытым источникам.\n\n"
        "⚠️ Бесплатные API дают ограниченные данные.\n"
        "Для полного пробива нужны платные сервисы.",
        reply_markup=phone_kb
    )

@dp.message(lambda msg: msg.contact is not None)
async def get_contact(message: types.Message):
    phone = message.contact.phone_number
    if not phone.startswith("+"):
        phone = "+" + phone
    await message.answer("⏳ Ищу информацию...")
    result = await search_phone(phone)
    await message.answer(f"🔍 Результат для {phone}:\n\n{result}")

@dp.message()
async def text_search(message: types.Message):
    text = message.text.strip()
    # Очистка номера
    clean = text.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if clean.startswith("+") or clean.startswith("8"):
        if len(clean) >= 10:
            await message.answer("⏳ Ищу информацию...")
            result = await search_phone(clean)
            await message.answer(f"🔍 Результат для {clean}:\n\n{result}")
        else:
            await message.answer("⚠️ Слишком короткий номер.")
    else:
        await message.answer("ℹ️ Введи номер в формате +7XXXXXXXXXX")

# ===== ВЕБ-СЕРВЕР =====
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
