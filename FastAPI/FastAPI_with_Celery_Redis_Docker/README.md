# Execution
Launch the redis server via docker by following steps on https://github.com/sameersbn/docker-redis
```
docker pull sameersbn/redis:4.0.9-2
```
```
#run the redis server
docker run --name redis -d --restart=always \
  --publish 6379:6379 \
  --volume /srv/docker/redis:/var/lib/redis \
  sameersbn/redis:4.0.9-2
```

```cd Celery_demo && celery -A task worker --pool=solo --loglevel=info```
Upon successful execution and connection with redis server, A similar log will be displayed in the tail of the verbose.

```
[tasks]                                                                                                  │
  . task.background_tasks                                                                                │
                                                                                                         │
[2021-02-13 11:20:26,911: INFO/MainProcess] Connected to redis://localhost:6379/0                        │
[2021-02-13 11:20:26,938: INFO/MainProcess] mingle: searching for neighbors                              │
[2021-02-13 11:20:28,002: INFO/MainProcess] mingle: all alone                                            │
[2021-02-13 11:20:28,139: INFO/MainProcess] celery@LAPTOP-95TSTULK ready.
```

Now open a python interpreter and add something to task queue
``` cd Celery_demo && python3```

```# Now execute the following
> from task import background_tasks
#i.e from task script import the function
#now attach it to the celery task using delay
> process = background_task.delay(3)
#3 is the arg of the function background_task
```

```
#Upon completion, the log of redis server should be like
[2021-02-13 11:27:40,385: WARNING/MainProcess] SubTask 0 out of 3 is executed                            │
[2021-02-13 11:27:43,389: WARNING/MainProcess] SubTask 1 out of 3 is executed                            │
[2021-02-13 11:27:46,393: WARNING/MainProcess] SubTask 2 out of 3 is executed                            │
[2021-02-13 11:27:46,419: INFO/MainProcess] Task task.background_tasks[2db65713-33a7-464c-8089-a3a208c0a2│
c8] succeeded in 9.035767600000327s: 'Task completed!'
```
```
#Now you can acess the process id, process status and process get to get the data
> process
> process.id
> process.status #this will yield either PENDING or SUCCESS.
> process.get() if process.status == SUCESSS

```
