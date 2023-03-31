#!/bin/bash
# Post to an arg URL and displays the response body
curl -s -X POST -d "email=test@gmail&subject=I will always be here for PLD" "$1"
