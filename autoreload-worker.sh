#!/bin/bash

# this is a really great thing from http://avilpage.com/2017/05/how-to-auto-reload-celery-workers-in-development.html
# now when changes are made, both flask AND the worker will auto-reload so you don't have to mash C-c and restart it
# yourself. basically, workflow upgraded.

# first, if you are not on macOS you'll need to do: pip install watchdog
# if you are on macOS, watchdog is because there have been bug fixes that aren't in the latest version release. instead
# you have to install it direct from the git repo and do: pip install git+https://github.com/gorakhargosh/watchdog.git

watchmedo auto-restart -d app/mod_check -p '*.py' -- celery worker -A app.mod_check
