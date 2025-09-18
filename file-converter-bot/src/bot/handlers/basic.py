from aiogram import Router, types
from aiogram.filters import CommandStart
router=Router()
@router.message(CommandStart())
async def start(msg:types.Message):
    await msg.answer('👋 Ready. Use /img2pdf /merge /compress /pdf2img')
