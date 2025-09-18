import os, subprocess, zipfile
from typing import List
from pypdf import PdfReader, PdfWriter
from pdf2image import convert_from_path
import img2pdf

def merge_pdfs(paths:List[str], out_path:str)->str:
    w=PdfWriter()
    for p in paths:
        r=PdfReader(p)
        [w.add_page(pg) for pg in r.pages]
    open(out_path,'wb').write(w.write_bytes()); return out_path

def images_to_pdf(imgs:List[str], out_path:str)->str:
    open(out_path,'wb').write(img2pdf.convert(imgs)); return out_path

def compress_pdf(inp:str, outp:str, quality:str='screen')->str:
    cmd=['gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.4',f'-dPDFSETTINGS=/{quality}','-dNOPAUSE','-dQUIET','-dBATCH',f'-sOutputFile={outp}',inp]; subprocess.run(cmd,check=True); return outp

def pdf_to_images_zip(pdf_path:str, out_zip:str, dpi:int=150)->str:
    imgs=convert_from_path(pdf_path,dpi=dpi)
    base=os.path.splitext(out_zip)[0]; os.makedirs(base,exist_ok=True)
    paths=[]
    for i,im in enumerate(imgs,1):
        p=os.path.join(base,f'page_{i:03d}.png'); im.save(p,'PNG'); paths.append(p)
    with zipfile.ZipFile(out_zip,'w',zipfile.ZIP_DEFLATED) as z:
        [z.write(p, arcname=os.path.basename(p)) for p in paths]
    return out_zip
