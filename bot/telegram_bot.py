import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import httpx
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from database.whitelist import is_user_allowed
from services.imei_validator import is_valid_imei

# Загружаем переменные окружения
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = "http://127.0.0.1:8000/api/check-imei"
API_TOKEN = os.getenv("API_TOKEN")

# Создаем бота и диспетчер
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Логирование
logging.basicConfig(level=logging.INFO)

# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Отправь мне IMEI, и я проверю его!")

# Обработчик IMEI
@dp.message()
async def check_imei(message: Message):
    user_id = message.from_user.id
    imei = message.text.strip()

    # Проверяем, есть ли пользователь в белом списке
    if not is_user_allowed(user_id):
        await message.answer("❌ У вас нет доступа к боту.")
        return

    # Проверяем валидность IMEI
    if not is_valid_imei(imei):
        await message.answer("⚠️ Некорректный IMEI! Он должен содержать 15 цифр и проходить проверку алгоритмом Луна.")
        return

    # Делаем запрос в API FastAPI
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(API_URL, json={"imei": imei, "token": API_TOKEN})

        if response.status_code == 200:
            data = response.json()
            text = f"📱 Бренд: {data['brand']}\n📌 Модель: {data['model']}\n✅ Статус: {data['status']}"
        else:
            text = "❌ Ошибка при проверке IMEI."

    except Exception as e:
        text = f"⚠️ Ошибка: {e}"

    # Отправляем пользователю ответ
    await message.answer(text)

# Запуск бота
async def main():
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
