# Hermes - How to Start Developing

Note: Ubuntu 16.04 was has been used exclusively for development so far which is what this guide caters to.

This documentation will be updated to support Ubuntu 18.04



## Install Pre-Requirements
- Python 3.6 (Required)
    - Ubuntu 16.04:
        ```
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt-get update
        sudo apt-get install python3.6 python3-pip
        ```
- Virtual Environments (Optional, but highly recommended)
    - Ubuntu:
        ```
        pip install virtualenv
        virtualenv --python=/usr/bin/python3.6 venv
        source venv/bin/activate
        ```

- Install External Requirements
    - Ubuntu:
        ```
        sudo apt-get install python3.6-dev libssl-dev
        ```
- Install Python Requirements
    - Ubuntu:
        ```
        pip install -r requirements.txt
        ```

## Running Dev Environment
**This will be updated to use docker-compose**

Currently the way we are running the development environment is with a docker image of RabbitMQ with its default ports being passed to the same external ports of the dev machine.  This configuration is used so each developer doesn't have to modify the `Hermes/app/mod_check/__init__.py` file.

### Steps
1) `sudo docker pull rabbitmq`
2) `sudo docker run -d -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 25672:25672 rabbitmq`
3) `./autoreload-worker.sh`
4) `./run.py`

The Celery workers and Flask application should now be started and able to connect to the RabbitMQ instance.
