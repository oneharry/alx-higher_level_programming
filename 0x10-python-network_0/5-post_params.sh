#!/bin/bash
# Post to an arg URL and displays the response body
curl -X POST -s -d "email=test@gmail&subject=I will always be here for PLD" "$1"
