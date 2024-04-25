#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
response=$(curl -s -w "%{http_code}" "$1")

# Extract the status code
status_code=$(echo "$response" | tail -n1)

# Check if the request was successful (status code 200)
if [ "$status_code" == "200" ]; then
    # Display the body of the response
    echo "$response" | head -n -1
fi
