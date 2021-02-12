#Example with Redis task queue
#mandatory imports
import uvicorn
from fastapi import FastAPI
import redis
from rq import Queue
import time
#creating an object of redis
redis_object = redis.Redis()
#creating a task queue object
q = Queue(connection=redis_object)
#creating an object of FastAPI
app = FastAPI()
#creating get, post methods for the app
@app.get('/'):
def index():
    return('Welcome to the Basic Task scheduling demo!')
