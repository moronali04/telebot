import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from yt_dlp import YoutubeDL

# Bot token
BOT_TOKEN = "7263584787:AAFt8RNh7lSHNCpc7ndotXhFLe6iXQHkFRg"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# YDL options
YDL_OPTS = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s',
    'noplaylist': True,
    'quiet': True,
    'no_warnings': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # or any format you prefer
    }],
}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "হ্যালো! এই বট ইউটিউব ভিডিও ডাউনলোড করে দিবে। শুধু ভিডিওর লিঙ্ক পাঠাও।"
    )

@dp.message_handler(regexp=r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/')
async def download_video(message: types.Message):
    url = message.text.strip()
    msg = await message.reply("ডাউনলোড শুরু হচ্ছে... ⏳")
    try:
        loop = asyncio.get_event_loop()
        # Download video
        info = await loop.run_in_executor(
            None,
            lambda: YoutubeDL(YDL_OPTS).extract_info(url, download=True)
        )
        filename = f"{info['id']}.{info['ext']}"
        # Send video
        await bot.send_video(
            message.chat.id,
            open(filename, 'rb'),
            caption=info.get('title', 'YouTube Video')
        )
        await msg.edit_text("🔽 ডাউনলোড সম্পূর্ণ! ভিডিও নিচে পেতে পারো।")
    except Exception as e:
        await msg.edit_text(f"ত্রুটি: {e}")
    finally:
        # Clean up file
        if 'filename' in locals() and os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
