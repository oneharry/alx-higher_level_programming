#!/bin/bash
# Sends request to URL and displays the status code
curl -sLI -w "%{http_code}" "$1"
