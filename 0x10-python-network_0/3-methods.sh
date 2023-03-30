#!/bin/bash
# Takes URL as args, displays all HTTP methods that server will accept
curl -X OPTIONS -siL "$1" | grep Allow: | cut -d : -f 2
