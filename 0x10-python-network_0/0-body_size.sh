#!/bin/bash
# Takes in URL as arhument, displays the size of the respinse body
curl -sI "$1" | grep -iF 'Content-Type' | cut -d ' ' -f 2
