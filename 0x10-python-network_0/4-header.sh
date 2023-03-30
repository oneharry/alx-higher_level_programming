#!/bin/bash
# Gets url, displays response body, and set header variable
curl -sL "$1" -H "X-School-User-Id=98"
