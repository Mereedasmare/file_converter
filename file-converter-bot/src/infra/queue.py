from redis import Redis
from rq import Queue
from ..domain.settings import Settings

def get_queue():
    s=Settings(); return Queue('default', connection=Redis.from_url(s.REDIS_URL))
