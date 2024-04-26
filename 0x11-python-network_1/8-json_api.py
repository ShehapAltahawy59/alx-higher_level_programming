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
    q=""
    if sys.argv >=2:
        q = sys.argv[2]
    r = requests.post("http://0.0.0.0:5000/search_user", params=q)
    print(r.text)
