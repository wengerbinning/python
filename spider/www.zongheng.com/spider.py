#!/usr/local/bin python3

"""纵横中文网全本全本小说

该项目实现纵横中文网全本小说的数据获取，url：<http://book.zongheng.com/store/c0/c0/b0/u0/p25/v9/s1/t0/u0/i1/ALL.html/>。
"""

__author__ = "Clark Aaron"
__version__ = "v0.0"

import requests

URL = "http://book.zongheng.com/store/c0/c0/b0/u0/p25/v9/s1/t0/u0/i1/ALL.html"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
}

def getIndex(url: str,headers: dict) -> str :
    response = requests.get(url,headers=headers)
    print(response.status_code)

    return response.text

def main():
    html = getIndex(URL,headers)
    print(html)

if __name__ == "__main__":
    main()