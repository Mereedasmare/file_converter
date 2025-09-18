import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from .handlers import basic, ops
from ..domain.settings import Settings
async def main():
    s=Settings(); bot=Bot(token=s.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp=Dispatcher(); dp.include_router(basic.router); dp.include_router(ops.router)
    await dp.start_polling(bot)
if __name__=='__main__': asyncio.run(main())
