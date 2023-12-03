# Найти бота @BotFather, написать ему /start, или /newbot, заполнить поля
# Доработаем бота. Сделаем сообщения более информатиынми, добавим ссылок в стиле html.

# MrKoKstelebot


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.types import FSInputFile   #, URLInputFile

# импорты
from config_reader import config

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    await message.answer(
        'перейти на сайт <a href="https://kokos.mozellosite.com">KoKos Mozellosite</a> \n'
        "Я бесполезный бот <u>Мистера КоКа</u>, и помогать тебе не собираюсь.\n"
        "Для справки <b>/help</b>",
        parse_mode=ParseMode.HTML
    )

# Хэндлер на команду /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Я бесполезный бот <u>Мистера КоКа</u>\n"
        "Музыка Хит-месяца <b>/music</b>\n"
        "Эмодзи <b>/dice</b>\n"
        '<a href="https://files.fm/u/aqw2p3uj">1_КУРС</a>\n'
        '<a href="https://files.fm/u/gqjv2wqqp">2_КУРС</a>\n'
        '<a href="https://files.fm/u/2bux9z5q">3_КУРС</a>\n'
        "Котлетки <b>/kotletki</b>\n",
        disable_web_page_preview=True,  # убрать превью ссылки
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



# Music

audio_mp3 = FSInputFile(
    'media/mot-sluchajjnosti-ne-sluchajjny.mp3',
#audio_mp3 = URLInputFile(
#    'https://cloud.mail.ru/public/UQ9u/DygGWtRtR',
    filename="Случайности не случайны"
)

@dp.message(Command("music"))
async def music(message: types.Message):
    await message.answer_audio(audio=audio_mp3, caption='` 😏 это тест`', parse_mode='MarkdownV2' ) # , title='Случайности не случайны'



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, skip_updates=True)  # не получать сообщения, когда был офлайн

if __name__ == "__main__":
    asyncio.run(main())
