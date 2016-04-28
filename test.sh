#!/bin/sh

set -e

flake8 app *.py

python run.py 2> /dev/null &
RUN_PID=$!

trap "kill $RUN_PID" EXIT

sleep 2

# Homepage should work
curl -sS "localhost:5000/" --fail > /dev/null
# Sending mail should return 502 as no mailer has been configured

curl -sS "localhost:5000/" -X POST -o /dev/null -w "%{http_code}\n" \
    --data "to_email=test@example.com&subject=test&body=testtest" | grep 502 > /dev/null
