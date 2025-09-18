from aiogram import Router, types, F
from aiogram.filters import Command
from ..keyboards.common import collector_kb
from ..utils.tg import download_file
from ...services.collector import CollectorManager
from ...infra.queue import get_queue
router=Router(); collector=CollectorManager()
@router.message(Command('img2pdf'))
async def img2pdf(msg:types.Message):
    j=collector.start(msg.from_user.id,msg.chat.id,'img2pdf')
    await msg.answer('Send images, then tap Done.', reply_markup=collector_kb(j.id))
@router.message(Command('merge'))
async def merge(msg:types.Message):
    j=collector.start(msg.from_user.id,msg.chat.id,'merge')
    await msg.answer('Send PDFs to merge, then tap Done.', reply_markup=collector_kb(j.id))
@router.callback_query(F.data.startswith('done:'))
async def done(cb:types.CallbackQuery):
    jid=cb.data.split(':',1)[1]; j=collector.get(jid)
    if not j or not j.input_assets: await cb.answer('No files.', show_alert=True); return
    await cb.message.edit_text('Processing...')
    q=get_queue()
    if j.type=='img2pdf':
        q.enqueue('file-converter-bot.src.workers.tasks.pdf_tasks.task_img2pdf', j.user_id, j.chat_id, j.id, [a.path for a in j.input_assets])
    if j.type=='merge':
        q.enqueue('file-converter-bot.src.workers.tasks.pdf_tasks.task_merge', j.user_id, j.chat_id, j.id, [a.path for a in j.input_assets])
    collector.pop(jid); await cb.answer('Started')
@router.message(F.document | F.photo)
async def on_file(msg:types.Message):
    j=None
    for _j in list(collector.jobs.values()):
        if _j.user_id==msg.from_user.id and _j.chat_id==msg.chat.id: j=_j
    if not j: return
    p=await download_file(msg.bot,msg,j.id)
    if p: collector.add_file(j.id,p)
@router.message(Command('compress'))
async def compress_cmd(msg:types.Message):
    await msg.reply("Send the PDF as a document with caption 'compress quality' (e.g., screen/ebook/printer).")
@router.message(F.caption.contains('compress'))
async def compress_upload(msg:types.Message):
    if not msg.document or msg.document.mime_type!='application/pdf':
        await msg.reply('Attach a PDF with caption, e.g., compress screen'); return
    qual=(msg.caption or 'compress screen').split()[1]
    from ...domain.models import Job
    j=Job(user_id=msg.from_user.id, chat_id=msg.chat.id, type='compress')
    p=await download_file(msg.bot,msg,j.id)
    get_queue().enqueue('file-converter-bot.src.workers.tasks.pdf_tasks.task_compress', j.user_id, j.chat_id, j.id, p, qual)
    await msg.reply('Compressing...')
@router.message(Command('pdf2img'))
async def pdf2img_cmd(msg:types.Message):
    await msg.reply("Send the PDF as a document with caption 'pdf2img'")
@router.message(F.caption.contains('pdf2img'))
async def pdf2img_upload(msg:types.Message):
    if not msg.document or msg.document.mime_type!='application/pdf':
        await msg.reply('Attach a PDF with caption pdf2img'); return
    from ...domain.models import Job
    j=Job(user_id=msg.from_user.id, chat_id=msg.chat.id, type='pdf2img')
    p=await download_file(msg.bot,msg,j.id)
    get_queue().enqueue('file-converter-bot.src.workers.tasks.pdf_tasks.task_pdf2img', j.user_id, j.chat_id, j.id, p, 150)
    await msg.reply('Converting to images...')
