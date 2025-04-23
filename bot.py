import asyncio
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

TOKEN = "7263584787:AAFt8RNh7lSHNCpc7ndotXhFLe6iXQHkFRg"
CHAT_ID = "@moron_ali"  # একক গ্রুপ বা ইউজারের chat id

messages = {
    "00": "রাত ১২টা বাজে, এখনো জাগো কেন?",
    "01": "রাত ১টা বাজে, একটু বিশ্রাম নাও।",
    "02": "রাত ২টা বাজে, গভীর রাত!",
    "03": "রাত ৩টা বাজে, ঘুমানো উচিত!",
    "04": "রাত ৪টা বাজে, ফজরের সময় কাছাকাছি।",
    "05": "ভোর ৫টা বাজে, নতুন দিনের শুরু!",
    "06": "সকাল ৬টা বাজে, উঠার সময়!",
    "07": "সকাল ৭টা বাজে, স্কুল বা কাজের প্রস্তুতি নাও।",
    "08": "সকাল ৮টা বাজে, সকালের ব্যস্ততা শুরু!",
    "09": "সকাল ৯টা বাজে, কাজে মনোযোগ দাও।",
    "10": "সকাল ১০টা বাজে, কফি ব্রেক টাইম!",
    "11": "সকাল ১১টা বাজে, সকাল প্রায় শেষ।",
    "12": "দুপুর ১২টা বাজে, লাঞ্চের প্রস্তুতি নাও।",
    "13": "দুপুর ১টা বাজে, নামাজ পড়ে নিও।",
    "14": "দুপুর ২টা বাজে, হালকা বিশ্রাম নাও।",
    "15": "বিকাল ৩টা বাজে, কাজ শেষের পথে।",
    "16": "বিকাল ৪টা বাজে, বিকেলের নাস্তা টাইম!",
    "17": "বিকাল ৫টা বাজে, আসরের সময়।",
    "18": "সন্ধ্যা ৬টা বাজে, নামাজ পড়ে নিও।",
    "19": "সন্ধ্যা ৭টা বাজে, পরিবারের সাথে সময় কাটাও।",
    "20": "রাত ৮টা বাজে, ডিনারের প্রস্তুতি নাও।",
    "21": "রাত ৯টা বাজে, বই পড়া বা বিশ্রামের সময়।",
    "22": "রাত ১০টা বাজে, ঘুমাতে যাও।",
    "23": "রাত ১১টা বাজে, আগামী দিনের প্রস্তুতি নাও।",
}

async def send_hourly_message():
    bot = Bot(token=TOKEN)
    while True:
        now = datetime.now()
        hour_str = now.strftime("%H")
        message = messages.get(hour_str)
        if message:
            try:
                await bot.send_message(chat_id=CHAT_ID, text=message)
                print(f"Sent message at {hour_str}:00")
            except TelegramError as e:
                print(f"Error sending message: {e}")
        await asyncio.sleep(3600 - now.minute * 60 - now.second)

if __name__ == "__main__":
    asyncio.run(send_hourly_message())
