#!/usr/bin python3

import ssl

from urllib import request

url = "https://fontawesome.com/"

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

context = ssl._create_unverified_context()

urler = request.Request(url, headers=headers)

req = request.urlopen(urler,context=context)

print(req.status)