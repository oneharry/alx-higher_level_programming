#!/bin/bash
# Post to an arg URL and displays the response body
curl -sX POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
