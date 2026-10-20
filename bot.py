import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8951516202:AAHMNyUKnA7kFP2YMICj5XHz4ezCEEGPgsY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚀 Study Bot WebApp ဖွင့်ရန်", web_app=WebAppInfo(url="https://moehankops-droid.github.io/study-bot/"))
    builder.button(text="👥 Join Group", url="https://t.me/-IX703z2qZNY2ZnE9")
    builder.adjust(1)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔴 EARN NOW")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "👋 **Welcome to Study Bot!**\n\nောက်ဆက်လက်လုပ်ကိုင်နိုင်ရန် Mini App ကို ဝင်ရောက်လေ့လာနိုင်ပြီ -",
        parse_mode="Markdown",
        reply_markup=builder.as_markup()
    )
    await message.answer("အောက်ပါ Menu ကိုလည်း အသုံးပြုနိုင်ပြီ -", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
