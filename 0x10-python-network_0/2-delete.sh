#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi
curl -s -X DELETE "$1"
