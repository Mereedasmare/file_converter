from rq import Connection, Worker, Queue
from redis import Redis
from ..domain.settings import Settings
s=Settings()
with Connection(Redis.from_url(s.REDIS_URL)):
    Worker([Queue('default')]).work(with_scheduler=True)
