#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
