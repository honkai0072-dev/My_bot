from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

TOKEN = "8717089842:AAHm4IKQS6A89LLcviSDYm5yyEA6j7WTHso"

bot = Bot(token=TOKEN)
dp = Dispatcher()

PHONE_DB = {
    "+79117670106": "Иван Петров, Москва",
    "+79512265847": "Мария Смирнова, СПб",
}

phone_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📱 Отправить номер", request_contact=True)]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Отправь номер телефона, я поищу в базе.",
        reply_markup=phone_kb
    )

@dp.message(lambda msg: msg.contact is not None)
async def get_contact(message: types.Message):
    phone = message.contact.phone_number
    if not phone.startswith("+"):
        phone = "+" + phone
    result = PHONE_DB.get(phone, f"❌ Номер {phone} не найден.")
    await message.answer(f"🔍 Результат:\n{result}")

@dp.message()
async def text_search(message: types.Message):
    text = message.text.strip()
    if text.startswith("+") or text.startswith("8"):
        clean = text.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if len(clean) >= 10:
            result = PHONE_DB.get(clean, f"❌ Номер {clean} не найден.")
            await message.answer(f"🔍 Результат:\n{result}")
        else:
            await message.answer("⚠️ Слишком короткий номер.")
    else:
        await message.answer("ℹ️ Отправь номер или нажми кнопку.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
