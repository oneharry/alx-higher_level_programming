#!/bin/bash
# Sends request that causes server respond with msg: "You got me"
curl -sXL PUT -d "user_id=98" -H "Origin:You got me!" "0.0.0.0:5000/catch_me"
