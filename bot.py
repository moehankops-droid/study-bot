import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

# Bot Token ကို ထည့်သွင်းပြီးပါပြီ
TOKEN = "8951516202:AAHMNyUKnA7kFP2YMICj5XHz4ezCEEGPgsY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Chat ထဲမှာ ပေါ်မယ့် ခလုတ်များ (Inline Buttons)
    builder = InlineKeyboardBuilder()
    builder.button(text="🎮 Open WebApp", web_app=WebAppInfo(url="https://your-website-url.com"))
    builder.button(text="💬 Join Group", url="https://t.me/your_group_link")
    builder.button(text="📢 Join Channel", url="https://t.me/your_channel_link")
    builder.adjust(1)
    
    # အောက်ခြေမှာ ပေါ်မယ့် Menu ခလုတ် (Reply Keyboard)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎯 EARN NOW")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "👋 Welcome to Study Bot!\n\nကျေးဇူးပြု၍ အောက်ပါခလုတ်များကို နှိပ်ပါ။",
        reply_markup=builder.as_markup()
    )
    await message.answer("အောက်ပါ Menu ကိုလည်း အသုံးပြုနိုင်ပါပြီ -", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    