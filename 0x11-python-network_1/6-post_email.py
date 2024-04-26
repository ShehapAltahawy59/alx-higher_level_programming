#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.get(sys.argv[1],data=payload)
    print(r.text)
