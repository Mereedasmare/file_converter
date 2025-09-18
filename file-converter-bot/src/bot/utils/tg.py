import os
from aiogram import Bot
from aiogram.types import Message
from ...infra.storage import user_job_dir
async def download_file(bot:Bot, msg:Message, job_id:str)->str|None:
    if not msg.document and not msg.photo: return None
    filename='file'
    if msg.document:
        tf=await bot.get_file(msg.document.file_id)
        filename=msg.document.file_name or filename
    else:
        ph=msg.photo[-1]; tf=await bot.get_file(ph.file_id); filename=f'photo_{ph.file_id}.jpg'
    dest=user_job_dir(msg.from_user.id, job_id)
    path=os.path.join(dest, filename)
    await bot.download_file(tf.file_path, destination=path)
    return path
