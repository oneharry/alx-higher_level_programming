#!/bin/bash
# Sends request to URL and displays the status code
curl -o /dev/null -sI -w "%{http_code}\n" "$1"
