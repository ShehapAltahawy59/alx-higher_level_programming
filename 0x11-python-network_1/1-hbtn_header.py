#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status
import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.info()
        x_request_id = data.get("X-Request-Id")
        print(x_request_id)
