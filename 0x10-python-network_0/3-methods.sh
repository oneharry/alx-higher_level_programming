#!/bin/bash
# Takes URL as args, displays all HTTP methods that server will accept
curl -sI "$1" | grep -i Allow | cut -d ' ' -f 2-
