#!/usr/local/bin python3
"""亚洲大学排名

获取usnews的亚洲大学排名，url：<https://www.usnews.com/education/best-global-universities/asia>
"""

__author__ = "Clark Aaron"
__version__ = "v0.0"

import re
import json
import requests

URL = "https://www.usnews.com/education/best-global-universities/asia"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}

def getIndex(url: str, headers: dict) -> str :
    response = requests.get(url,headers=headers)
    print(response.status_code)
    return response.text

def parseHTML(html: str) -> str :
    dataPattern = r"window\['__PAGE_CONTEXT_QUERY_STATE__'\]\s=\s(.*?)\n"
    data = re.search(dataPattern,html)
    return data.group(1)

    return None
    
def main():
    html = getIndex(URL,headers)
    jsonContent = parseHTML(html)[:-1]
    data = json.loads(jsonContent)
    data = data["src/containers/pages/education/higher-education/global-universities/search/index.js"]
    data = data["data"]["items"]
    for university in data:
        name = university["name"] 
        city = university["city"]
        stats = university["stats"]
        ranks = university["ranks"]
        country = university["country_name"]
        print(name,country,city,ranks[0]["value"])            
        
    


if __name__ == "__main__":
    main()
