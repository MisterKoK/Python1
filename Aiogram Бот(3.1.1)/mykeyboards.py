from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

'''
def initial_keyboard():
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard_markup.insert(types.InlineKeyboardButton(text='Ru🇷🇺 to En🇬🇧 Vi🇻🇳', callback_data=f'Rus_to_EnVi'))
    keyboard_markup.insert(types.InlineKeyboardButton(text='Vi🇻🇳 to En🇬🇧 Ru🇷🇺 ', callback_data=f'Vi_to_EnRu'))
    keyboard_markup.insert(types.InlineKeyboardButton(text='Переводчик', callback_data=f'translate'))
    return keyboard_markup

'''
# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='Ru🇷🇺 to En🇬🇧 Vi🇻🇳',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='Vi🇻🇳 to En🇬🇧 Ru🇷🇺',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)