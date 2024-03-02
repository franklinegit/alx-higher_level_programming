#!/usr/bin/python3

import requests

try:
    response = requests.get("http://example.com")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")