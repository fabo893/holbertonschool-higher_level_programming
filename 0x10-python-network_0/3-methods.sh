#!/bin/bash
# Curl only methods
curl -siX OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
