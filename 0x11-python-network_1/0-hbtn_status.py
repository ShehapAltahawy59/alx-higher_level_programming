#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf_content=response.read().decode("utf-8")
    

print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}\n\t- utf8 content: {utf_content}")
