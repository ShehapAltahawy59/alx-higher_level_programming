#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import requests
import sys

r = requests.get(sys.argv[1]).headers
print(r.get("X-Request-Id"))
