#!/bin/bash
# Gets url, displays response body, and set header variable
curl -sL -H "X-School-User-Id: 98" "$1"
