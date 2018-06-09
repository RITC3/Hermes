# Hermes

Hermes is a scoring engine written purely in Python. This project is a direct result
of trying to easily score and track service uptime for Attack-Defense competitions.
Hermes tries to be hip and modern by using Python 3, RabbitMQ + Celery, and probably
some other things I am forgetting about.


## [Installing for Development](./Hermes_Dev.md)


## Setting up RabbitMQ
Hermes uses RabbitMQ as a message broker for service checking. Celery workers from
multiple locations can receive tasks from the queue which helps prevent bottlenecks.
Docker has been the simplest way to run RabbitMQ, especially during development.
[This](https://hub.docker.com/r/_/rabbitmq/) is the official RabbitMQ Docker repository
and can be used out-of-the-box for this.



### Starting Workers
Workers are used by RabbitMQ to execute tasks. When a task has been sent to RabbitMQ,
it is added into the queue. Then, the tasks are distributed to available workers. In
order for Hermes to check services, there must be at least one worker connected.   


Hermes utilizes Celery for workers and tasks  

To start a single worker:
```bash
$ celery worker --app=app.mod_check
```

To start, stop, and restart multiple workers:
```bash
# start 5 workers
$ celery multi start 5 --app=app.mod_check

# stop 5 workers
$ celery multi stop 5 --app=app.mod_check

# restart 5 workers
$ celery multi restart 5 --app=app.mod_check
``` 

To use a different broker address or a different broker entirely, look at the
`--broker` option for `celery`.

There is also a script included called `autoreload-worker.sh` which will
automatically reload the celery worker if there have been code changes
(similar to running flask in debug mode). This will make the development
process much simpler as everything will automatically reload itself. 


## Running Hermes
Generally, to run Hermes:

1. Start RabbitMQ server
2. `cd path/to/Hermes`
3. `celery multi start 5 --app=app.mod_check` or `bash autoreload-worker.sh`
4. `python3 run.py`
