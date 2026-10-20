import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8951516202:AAHMnyUkNa7kFP2YMiCj5H3r4erCEEGPgsY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚀 Study Bot WebApp ဖွင့်ရန်", web_app=WebAppInfo(url="https://moehankops-droid.github.io/Study-everthing/"))
    builder.button(text="💬 Join Group", url="https://t.me/+IX703z2qZNY2ZmE9")
    builder.adjust(1)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎯 EARN NOW")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "👋 **Welcome to Study Bot!**\n\nအောက်ပါခလုတ်ကိုနှိပ်၍ Mini App ကို ဝင်ရောက်လေ့လာနိုင်ပါပြီ -",
        parse_mode="Markdown",
        reply_markup=builder.as_markup()
    )
    await message.answer("အောက်ပါ Menu ကိုလည်း အသုံးပြုနိုင်ပါပြီ -", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
