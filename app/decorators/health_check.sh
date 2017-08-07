#!/usr/bin/env bash
# this script is use to do health check, run python function in command
# require manage.py(flask) shell, ipython
exec env/bin/python manage.py shell << EOF
 from app.health.health_check import main
 main()
 quit
 EOF
