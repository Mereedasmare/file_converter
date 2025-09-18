from pydantic import BaseModel, Field
from typing import Literal, List
import uuid
JobType=Literal['img2pdf','merge','split','pdf2img','compress']
class FileAsset(BaseModel): id:str=Field(default_factory=lambda:uuid.uuid4().hex[:10]); path:str
class Job(BaseModel): id:str=Field(default_factory=lambda:uuid.uuid4().hex[:10]); user_id:int; chat_id:int; type:JobType; input_assets:List[FileAsset]=[]
