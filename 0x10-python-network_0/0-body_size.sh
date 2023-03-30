#!/bin/bash
# Takes in URL as arhument, displays the size of the respinse body
curl -sL "$1" | wc -c
