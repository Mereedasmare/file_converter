from pydantic import BaseModel
import os
class Settings(BaseModel):
    BOT_TOKEN: str = os.getenv('BOT_TOKEN','')
    REDIS_URL: str = os.getenv('REDIS_URL','redis://localhost:6379/0')
    STORAGE_ROOT: str = os.getenv('STORAGE_ROOT','/data/jobs')
