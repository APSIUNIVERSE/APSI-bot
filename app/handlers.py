from aiogram import F, Router, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType, InputFile
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from app.keyboards import main
from app.states import FigmaTask, TildaTask, BotTask

MANAGER_ID = ...

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
'''Привет! 👋

Добро пожаловать в бота A.P.S.I. Мы предлагаем следующие услуги:

🌐 Создание сайтов на Tilda: Идеальные сайты для вашего бизнеса, блога или проекта.

🎨 Дизайн в Figma: Красивые и функциональные макеты для любых нужд.

🤖 Разработка телеграм ботов: Автоматизация и новые возможности для вашего бизнеса.

Выберите одну из опций ниже, чтобы начать:''', reply_markup=main)


@router.callback_query(F.data == 'Figma')
async def order_figma_callback(callback: CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        await callback.message.answer('Отличный выбор! 🌟\n\nМы рады, что вы решили заказать дизайн в Figma. Чтобы начать работу над вашим проектом, нам нужно собрать немного информации.\n\nПожалуйста, ответьте на следующие вопросы:\n\n1) Опишите ваш проект\n\n2) Какой дизайн вам нужен? (дизайн сайта / приложения)\n\n3) Ссылки на ваших конкурентов?\n\n4) Нужна ли мобильная адаптация?\n\n5) Какие материалы для дизайна уже имеются?\n\n<b>Отправьте ответ на все вопросы в одном сообщении</b>', parse_mode='html')
        await callback.answer('')
        await state.set_state(FigmaTask.Brief)


@router.message(FigmaTask.Brief)
async def brief(message: Message, state: FSMContext):
    if message.text:
        username = message.from_user.username
        if username:
            from config import bot
            await bot.send_message(MANAGER_ID, text=f'Заказ: Дизайн в Figma\nПользователь @{username} заполнил бриф:\n {message.text}')
            await message.answer('Спасибо! С Вами скоро свяжется специалист')
            await state.clear()
        else:
            await bot.send_message(MANAGER_ID, text=f'Заказ: Дизайн в Figma\nПользователь заполнил бриф:\n {message.text}\n\nЖдем его номер телефона!')
            await message.answer('Кажется, у вас нет имени пользователя в аккаунте телеграм\nВведите ваш номер телефона или другой метод связи')
            await state.set_state(FigmaTask.Number)

            
@router.message(FigmaTask.Number)
async def number(message: Message, state:FSMContext):
    if message.text:
        from config import bot
        await bot.send_message(MANAGER_ID, text=f'Связь с заказчиком:\n{message.text}')
        await message.answer('Спасибо! С Вами скоро свяжется специалист')
        await state.clear()
        


@router.callback_query(F.data == 'Tilda')
async def tilda_callback(callback: CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        await callback.message.answer('Отличный выбор! 🌟\n\nМы рады, что вы решили заказать сайт на Tilda. Чтобы начать работу над вашим проектом, нам нужно собрать немного информации.\n\nПожалуйста, ответьте на следующие вопросы:\n\n1) Опишите ваш проект\n\n2) Какие цели будут у вашего сайта?\n\n3) Ссылки на ваших конкурентов?\n\n4) Какой функционал должен быть на сайте?\n\n5) Какие материалы для сайта уже имеются?\n\n<b>Отправьте ответ на все вопросы в одном сообщении!</b>', parse_mode='HTML')
        await callback.answer('')
        await state.set_state(TildaTask.Brief)


@router.message(TildaTask.Brief)
async def brief(message: Message, state: FSMContext):
    if message.text:
        username = message.from_user.username
        if username:
            from config import bot
            await bot.send_message(MANAGER_ID, text=f'Заказ: Сайт Tilda\nПользователь @{username} заполнил бриф:\n {message.text}')
            await message.answer('Спасибо! С Вами скоро свяжется специалист')
            await state.clear()
        else:
            await bot.send_message(MANAGER_ID, text=f'Заказ: Сайт Tilda\nПользователь заполнил бриф:\n {message.text}\n\nЖдем его номер телефона!')
            await message.answer('Кажется, у вас нет имени пользователя в аккаунте телеграм\nВведите ваш номер телефона или другой метод связи')
            await state.set_state(TildaTask.Number)


@router.message(TildaTask.Number)
async def number(message: Message, state:FSMContext):
    if message.text:
        from config import bot
        await bot.send_message(MANAGER_ID, text=f'Связь с заказчиком:\n{message.text}')
        await message.answer('Спасибо! С Вами скоро свяжется специалист')
        await state.clear()


@router.callback_query(F.data == 'Bot')
async def bot_callback(callback: CallbackQuery, state: FSMContext):
   if await state.get_state() is None:
        await callback.message.answer('Отличный выбор! 🌟\n\nМы рады, что вы решили заказать разработку телеграм бота. Чтобы начать работу над вашим проектом, нам нужно собрать немного информации.\n\nПожалуйста, ответьте на следующие вопросы:\n\n1. Опишите ваш проект\n\n2. Какие цели будут у бота\n\n3. Ссылки на ваших конкурентов\n\n4. Нужна ли поддержка после запуска бота?\n\n<b>Отправьте ответ на все вопросы в одном сообщении</b>', parse_mode="html")
        await callback.answer('')
        await state.set_state(BotTask.Brief)


@router.message(BotTask.Brief)
async def brief(message: Message, state: FSMContext):
    if message.text:
        username = message.from_user.username
        if username:
            from config import bot
            await bot.send_message(MANAGER_ID, text=f'Заказ: Бот тг\nПользователь @{username} заполнил бриф:\n {message.text}')
            await message.answer('Спасибо! С Вами скоро свяжется специалист')
            await state.clear()
        else:
            await bot.send_message(MANAGER_ID, text=f'Заказ: Бот тг\nПользователь заполнил бриф:\n {message.text}\n\nЖдем его номер телефона!')
            await message.answer('Кажется, у вас нет имени пользователя в аккаунте телеграм\nВведите ваш номер телефона или другой метод связи')
            await state.set_state(BotTask.Number)


@router.message(BotTask.Number)
async def number(message: Message, state:FSMContext):
    if message.text:
        from config import bot
        await bot.send_message(MANAGER_ID, text=f'Связь с заказчиком:\n{message.text}')
        await message.answer('Спасибо! С Вами скоро свяжется специалист')
        await state.clear()