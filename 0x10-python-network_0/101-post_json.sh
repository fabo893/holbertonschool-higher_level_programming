#!/bin/bash
# Curl a JSON file
value=`cat $2`
curl -sX POST "$1" -H "Content-Type: application/json" -d "$value"
