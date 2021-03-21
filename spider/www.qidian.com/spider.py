#!/usr/local/bin python3

"""起点中文网全本小说

该项目实现起点中文网全本小说的数据获取，url：<https://www.qidian.com/finish/>。
"""

__author__ = "Clark Aaron"
__version__ = "v0.0"

import redis
from urllib import (
    request,
    parse
)
from bs4 import BeautifulSoup

URL = "https://www.qidian.com/finish/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}


def getIndex(url: str, headers: dict) -> str:
    """获取url对应的html源码并返回。
    
    * url: 用户指定的页面地址，将请求页面的html源码并返回
    * return：返回str
    """
    urler = request.Request(url,headers=headers)
    response = request.urlopen(urler)
    print(response.getcode())
    return response.read().decode("utf-8")

def parserHTML(html: str) -> str:
    """使用BeautifulSoup解析HTML

    使用BeautifulSoup解析HTML,提取小说列表信息
    """
    books = []
    soup = BeautifulSoup(html,"html.parser")
    tags = soup.find_all("div",class_="book-mid-info")
    for book in tags:
        name = book.find('a',attrs={"data-eid":"qd_B58"})
        author = book.find('a',attrs={"data-eid":"qd_B59"}) 
        books.append({"name":name.string,"author":author.string,"url":name['href']})
    return books

def saveBook(books: tuple) -> bool:
    dataBase = redis.Redis(host="127.0.0.1",port=6379,db=0
    )
    for book in books:
         dataBase.hset(book['name'],"author",book['author'])  
         dataBase.hset(book['name'],"url",book['url'])
       
       

def main():
    for index in range(1,6):
        data = "?page=%s"%index
        url = parse.urljoin(URL,data)
        html = getIndex(url,headers)
        books = parserHTML(html)
        saveBook(books)

if __name__ == "__main__":
    main()