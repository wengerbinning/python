#!/usr/local/bin python3

from urllib import parse
from urllib import request

__URL__ = "https://haokan.baidu.com"


url = parse.urljoin(__URL__,"v?vid=5333429003649053425&pd=bjh&fr=bjhauthor&type=video")

print(url)

urler = request.Request(url)

# res = request.urlopen(urler)