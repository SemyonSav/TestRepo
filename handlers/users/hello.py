from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None, text='Привет')
async def bot_echo(message: types.Message):
    await message.answer("Привет")
