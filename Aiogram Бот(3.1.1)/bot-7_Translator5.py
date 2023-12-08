# Найти бота @BotFather, написать ему /start, или /newbot, заполнить поля
# https://kokos.mozellosite.com/
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

import mykeyboards

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# Диспетчер
dp = Dispatcher()

#========= Состояния
from aiogram.fsm.state import State, StatesGroup
class Form(StatesGroup):
    text_to_translate = State()
    text_to_translate2 = State()
#========

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
    )
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
        "Котлетки <b>/kotletki</b>\n"
        "Расписание <b>/schedule</b>\n"
        "Переводчик <b>/translate</b>\n",
        disable_web_page_preview=True,  # убрать превью ссылки
        parse_mode=ParseMode.HTML
    )

# Хэндлер на команду /schedule
@dp.message(Command("schedule"))
async def cmd_help(message: types.Message):
    await message.answer(
        "<b>Расписание</b>\n"
        '1 урок 8.30 - 9.15\n'
        '2 урок 9.30 - 10.15\n'
        '3 урок 10.20 - 11.05\n'
        '4 урок 11.10 - 11.55\n'
        '5 урок 12.15 - 13.00\n'
        '6 урок 13.05 - 13.50\n'
        '7 урок 13.55 - 14.40\n'
        '8 урок 14.45 - 15.30\n',
        disable_web_page_preview=True,  # убрать превью ссылки
        parse_mode=ParseMode.HTML
    )

# Добавлять эмодзи
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

# Кнопки котлетки ============
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

# Отправка Music =======================
audio_mp3 = FSInputFile(
    'media/mot-sluchajjnosti-ne-sluchajjny.mp3',
#audio_mp3 = URLInputFile(
#    'https://cloud.mail.ru/public/UQ9u/DygGWtRtR',
    filename="Случайности не случайны"
)

@dp.message(Command("music"))
async def music(message: types.Message):
    await message.answer_audio(audio=audio_mp3, caption='` 😏 это тест`', parse_mode='MarkdownV2' ) # , title='Случайности не случайны'

# Отправка фото ===================
@dp.message(Command('photo'))
async def get_photo(message: types.Message):
    await message.answer_photo(photo=FSInputFile('media/1.jpg', filename='Снеговик'), caption='Это снеговик!')

# Переводчик ======================
@dp.message(Command("translate"))
async def start_translate(message: types.Message):
    await message.answer("Как будем переводить?", reply_markup= mykeyboards.keyboard)

# НАЖАТИЕ ИНЛАЙН КНОПОК
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
# КНОПКА 1
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery, state: FSMContext):
    if callback.message.text != 'TRANSLATE FROM RUSSIAN':
        await callback.message.edit_text(
            text='TRANSLATE FROM RUSSIAN',
            reply_markup=callback.message.reply_markup
        )
    #await callback.answer()
    await state.set_state(Form.text_to_translate)
    #await Form.text_to_translate.state
    #await message.answer("Как будем переводить?", reply_markup= mykeyboards.keyboard)
from aiogram.filters import StateFilter
@dp.message(StateFilter(Form.text_to_translate))
async def send_translate_text(message: types.Message, state: FSMContext):
    from translate import trans
    translated_text = trans(message.text)
    #print(message.text)
    print(translated_text)
    await message.answer(text=f'{translated_text[0]}\n{translated_text[-1]}')
    await message.answer("ПереводчикRu")

# КНОПКА 2
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery, state: FSMContext):
    if callback.message.text != 'TRANSLATE FROM VIETNAMESE':
        await callback.message.edit_text(
            text='TRANSLATE FROM VIETNAMESE',
            reply_markup=callback.message.reply_markup
        )
    # await callback.answer()
    await state.set_state(Form.text_to_translate2)
@dp.message(StateFilter(Form.text_to_translate2))
async def send_translate_text(message: types.Message, state: FSMContext):
    from translate import transru
    translated_text = transru(message.text)
    print(translated_text)
    await message.answer(text=f'{translated_text[0]}\n{translated_text[-1]}')
    await message.answer("ПереводчикVi")
# Конец Переводчика =============================



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, skip_updates=True)  # не получать сообщения, когда был офлайн

if __name__ == "__main__":
    asyncio.run(main())
