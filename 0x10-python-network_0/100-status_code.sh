#!/bin/bash
# Sends request to URL and displays the status code
curl -o /dev/null -s -w "%{http_code}" "$1"
