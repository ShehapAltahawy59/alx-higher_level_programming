#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status').text
print(f"Body response:\n\t- type: {type(r)}\n\t- content: {r}")
