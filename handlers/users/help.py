from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/check - Checking")
    
    await message.answer("\n".join(text))


@dp.message_handler(Command("check"))
async def bot_help(message: types.Message):
    await message.answer("Checking")
