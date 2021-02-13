from time import sleep
import time
import redis
from celery import Celery
#creating the instance of selery
celery = Celery('task',backend='redis://localhost/0',broker='redis://localhost/0' )

#creating a background process to append it into the queue
#assigning background_task as celery task
@celery.task()
def background_tasks(n):
    delay = 5
    for i in range(n):
        time.sleep(n)
        print("SubTask {0} out of {1} is executed".format(i,n))
    return("Task completed!")

#execute via terminal
#celery -A task worker --pool=solo --loglevel=info


