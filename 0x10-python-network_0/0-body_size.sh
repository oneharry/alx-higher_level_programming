#!/bin/bash
# Takes in URL as arhument, displays the size of the respinse body
curl -sI "$1" | wc -c
