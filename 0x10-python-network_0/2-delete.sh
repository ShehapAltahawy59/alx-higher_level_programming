#!/bin/bash
# Check if URL has been provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

# Send DELETE request and display body of the response
curl -s -X DELETE "$1"
