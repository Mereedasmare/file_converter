from aiogram import Bot
from aiogram.types import FSInputFile
from ..domain.settings import Settings
s=Settings()
async def send_document(chat_id:int, path:str, caption:str=''):
    bot=Bot(token=s.BOT_TOKEN)
    try:
        await bot.send_document(chat_id, FSInputFile(path), caption=caption)
    finally:
        await bot.session.close()
