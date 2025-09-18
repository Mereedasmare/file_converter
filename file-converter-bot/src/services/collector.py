from ..domain.models import Job, FileAsset
class CollectorManager:
    def __init__(self): self.jobs={}
    def start(self,uid:int,cid:int,typ:str)->Job:
        j=Job(user_id=uid,chat_id=cid,type=typ); self.jobs[j.id]=j; return j
    def add_file(self,jid:str,path:str): self.jobs[jid].input_assets.append(FileAsset(path=path))
    def get(self,jid:str): return self.jobs.get(jid)
    def pop(self,jid:str): return self.jobs.pop(jid,None)
