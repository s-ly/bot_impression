import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import tokens

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
# bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
token_bot = tokens.token_SergeyLysovTestBot
bot = Bot(token=token_bot)

# Диспетчер
dp = Dispatcher()


# Отвечает на команду /start.
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Отвечает на все команды, должен стоять внизу.
@dp.message()
async def cmd_all(message: types.Message):
    await message.answer("All!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
