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
task_queue = Queue(connection=redis_object)
#creating an object of FastAPI
app = FastAPI()
#creating get, post methods for the app
@app.get('/')
def index():
    return('Welcome to the Basic Task scheduling demo!')

def task_scheduler_background(num_tasks):
    count = 0
    #simulating a fake processing delay
    time.sleep(2)
    #returning
    print("The task is in queue: Status {0} processed !".format(num_tasks))

@app.get('/add_task')
#now writing the second method
def add_task(num_tasks: int):
    job = task_queue.enqueue(task_scheduler_background, num_tasks)
    queue_length = len(task_queue)
    return {"{0} is being processed out of {1} tasks in the queue".format(job.id,queue_length)}
    #return {"This is {0}".format(num_tasks)}





if __name__ == '__main__':
    uvicorn.run(app,'127.0.0.1')


