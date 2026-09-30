# import asyncio
# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart
# from aiogram.types import Message

# TOKEN = "8618817430:AAGX9NSy2AGtOEr2PRXCjuq_HIwJDj8ToTs"

# bot = Bot(token=TOKEN)
# dp = Dispatcher()


# @dp.message(CommandStart())
# async def start_handler(message: Message):
#     await message.answer("Salom! Men sizning birinchi Aiogram botingizman 🤖")


# async def main():
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8618817430:AAGX9NSy2AGtOEr2PRXCjuq_HIwJDj8ToTs8python main.py"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Salom! 👋\n"
        "Men savol-javob botiman.\n"
        "Menga savolingizni yozing."
    )


@dp.message()
async def question_handler(message: Message):
    if message.text == "Isming nima?":
        await message.answer("Mening ismim Savol-Javob Bot 🤖")
    elif message.text == "Aiogram nima?":
        await message.answer(
            "Aiogram — Python yordamida Telegram botlar yaratish uchun kutubxona."
        )
    else:
        await message.answer(
            "Kechirasiz, bu savolga hozircha javobim yo‘q."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
