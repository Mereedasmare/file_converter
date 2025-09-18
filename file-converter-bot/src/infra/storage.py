import os, shutil
from ..domain.settings import Settings
s=Settings()

def user_job_dir(uid:int, jid:str)->str:
    p=os.path.join(s.STORAGE_ROOT,str(uid),jid); os.makedirs(p,exist_ok=True); return p
