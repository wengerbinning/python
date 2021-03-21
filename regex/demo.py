#！/usr/local/bin python3

""" Regular Expression

演示re库的使用方法
"""

__author__ = "Clark Aaron"
__version__ = "v0.0"

import re

string = """
Hey ClarkAaron-JH!

A third-party OAuth application (Docker Hub Builder) with repo scope was recently authorized to access your account.
Visit https://github.com/settings/connections/applications/8b6dc7da03f38fe914a3 for more information.

To see this and other security events for your account, visit https://github.com/settings/security

If you run into problems, please contact support by visiting https://github.com/contact

Thanks,
The GitHub Team
"""


namePattern = r".*?Hey\s(.*?)\s"
urlPattern = r"(https.*?)\s"
authorPattern = r"Thanks.*?The(.*?)$"

name = re.match(namePattern,string,re.S)
name = name.group()[5:-2]

url = re.search(urlPattern,string)
url = url.groups()

urls = re.findall(urlPattern,string)

author = re.search(authorPattern,string,re.S)
author = author.groups()

print(name)
print(url)
print(urls)
print(author)