#!/usr/local/bin python3
"""网络爬虫实验室

测试学习的爬虫技术，url：<http://www.httpbin.org/>
"""

__author__ = "Clark Aaron"
__version__ = "v0.0"

import requests
from bs4 import BeautifulSoup

URL = "http://www.httpbin.org/get"

def getIndex(url:str, headers: dict = None) -> str :
    response = requests.get(url)
    print(response.status_code)
    for key,value in response.headers.items():
        print(key,"----->",value)
    return response.text

def parseHTML(html: str) -> tuple :
    soup = BeautifulSoup(html)


def main():
    html = getIndex(URL)
    print(html)

if __name__ == "__main__":
    main()


