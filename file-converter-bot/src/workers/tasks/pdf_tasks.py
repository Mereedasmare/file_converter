import os, asyncio
from ...infra.notifier import send_document
from ...services import pdf_ops
from ...infra.storage import user_job_dir

def task_img2pdf(user_id:int, chat_id:int, job_id:str, images:list[str]):
    out=os.path.join(user_job_dir(user_id,job_id),'output.pdf')
    pdf_ops.images_to_pdf(images,out); asyncio.run(send_document(chat_id,out,'✅ Images → PDF'))

def task_merge(user_id:int, chat_id:int, job_id:str, pdfs:list[str]):
    out=os.path.join(user_job_dir(user_id,job_id),'merged.pdf')
    pdf_ops.merge_pdfs(pdfs,out); asyncio.run(send_document(chat_id,out,'✅ Merged PDF'))

def task_compress(user_id:int, chat_id:int, job_id:str, pdf_path:str, quality:str='screen'):
    out=os.path.join(user_job_dir(user_id,job_id),'compressed.pdf')
    pdf_ops.compress_pdf(pdf_path,out,quality); asyncio.run(send_document(chat_id,out,f'✅ Compressed ({quality})'))

def task_pdf2img(user_id:int, chat_id:int, job_id:str, pdf_path:str, dpi:int=150):
    out=os.path.join(user_job_dir(user_id,job_id),'pages.zip')
    pdf_ops.pdf_to_images_zip(pdf_path,out,dpi); asyncio.run(send_document(chat_id,out,'✅ PDF → Images (ZIP)'))
