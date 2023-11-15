
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import F


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="665")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    await message.answer(
        "Сообщение с <u>HTML-разметкой</u> \n"
        "Сообщение2 с <b>HTML-разметкой</b>",
        parse_mode=ParseMode.HTML
    )

# Добавлять эмодзи
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

# Кнопки
@dp.message(Command("kotletki"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    #await message.reply("Отличный выбор!")
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно! Бери с пюрешкой!")
    #await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, skip_updates=True)  # не получать сообщения, когда был офлайн

if __name__ == "__main__":
    asyncio.run(main())
