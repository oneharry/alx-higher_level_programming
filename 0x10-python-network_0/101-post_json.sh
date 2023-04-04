#!/bin/bash
# Sends request to POST to URL and display the body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
