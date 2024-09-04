from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создание дизайна в Figma', callback_data='Figma')],
    [InlineKeyboardButton(text='Создание сайта на Tilda', callback_data='Tilda')],
    [InlineKeyboardButton(text='Создание бота в Telegram', callback_data='Bot')]
])
