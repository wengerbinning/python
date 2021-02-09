# 数据分析

[//]: # (__author__ = "Clark Aaron")
[//]: # (__version__ = "v0.0")

数据分析是人工智能、大数据决策等应用的基础，对大量数据的特征进行提取，共分为数据获取、数据分析与数据可视化三部分。

## 数据获取

数据获取是进行数据分析的前提，而数据的获取需要借助爬虫的技术来获取；网络爬虫(Web Crawler)是一种按照一定规则,自动地爬取万维网信息的程序或脚本,在FOAF社区被称为网页追逐者;其过程主要分为数据请求、数据响应、数据解析、数据存储。

### 数据请求

在数据请求时我们需要向服务器发送请求，通常使用一些扩展模块来完成该任务，共分为静态页面、动态页面请求。

* 在Python中，我们可以使用requests、urllib等库实现该任务。
* 在requests库中，我们可以使用request()、get()、head()、post()、patch()、delete()来请求数据

### 数据响应

在我们向服务器发送后，经过服务器处理后会返回一个响应；如果请求成功，在响应中会包含我们所需的数据，而我们需要通过响应的状态码来判断请求失败的原因。

* 通用的状态码说明：

| 状态码 | 说明 | 状态码 | 说明 | 状态码 | 说明 | 状态码 | 说明 |
|:------:|:--- |:------:|:---- |:-----:|:---- |:-----:|:---- |
| 200 | 请求成功 | 300 | | 

### 数据解析

在获取到正确的响应后,我们需要解析出我们需要的数据。

* 在Python中，根据数据的特点,我们可以使用直接处理、JSON解析、正则表达式、$BeautifulSoup$、$PyQuery$、$XPat$来解析数据。

### 数据存储

* 
---
* selenium库
* phantomJS库
* pyquery库
* 



### Urllib库

* **`request` module**: defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

> * **[function]** `urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)`Open the URL url, which can be either a string or a Request object.
>
>   1. `url`: can be either a string or a Request object.
>   2. `data`: must be an object specifying additional data to be sent to the server, or None if no such data is needed. See Request for details.
>   3. `timeout`: The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). This actually only works for HTTP, HTTPS and FTP connections.
>   4. `cafile`: cafile should point to a single file containing a bundle of CA certificates.
>   5. `capath`: capath should point to a directory of hashed certificate files.
>    
>   * Deprecated since version 3.6: cafile, capath and cadefault are deprecated in favor of context. Please use ssl.SSLContext.load_cert_chain() instead, or let ssl.create_default_context() select the system’s trusted CA certificates for you.
> 
> * **[function]** `install_opener(opener)`: Install an OpenerDirector instance as the default global opener. Installing an opener is only necessary if you want urlopen to use that opener; otherwise, simply call OpenerDirector.open() instead of urlopen(). The code does not check for a real OpenerDirector, and any class with the appropriate interface will work.
> 
> * **[function]** `build_opener([handler, ...])`Return an OpenerDirector instance, which chains the handlers in the order given. handlers can be either instances of BaseHandler, or subclasses of BaseHandler (in which case it must be possible to call the constructor without any parameters). Instances of the following classes will be in front of the handlers, unless the handlers contain them, instances of them or subclasses of them: ProxyHandler (if proxy settings are detected), UnknownHandler, HTTPHandler, HTTPDefaultErrorHandler, HTTPRedirectHandler, FTPHandler, FileHandler, HTTPErrorProcessor.
>
> * **[function]** `pathname2url(path)`Convert the pathname path from the local syntax for a path to the form used in the path component of a URL. This does not produce a complete URL. The return value will already be quoted using the quote() function.
> * **[function]** `url2pathname(path)`Convert the path component path from a percent-encoded URL to the local syntax for a path. This does not accept a complete URL. This function uses unquote() to decode path.
> 
> * **[function]** `getproxies()`This helper function returns a dictionary of scheme to proxy server URL mappings. It scans the environment for variables named <scheme>_proxy, in a case insensitive approach, for all operating systems first, and when it cannot find it, looks for proxy information from Mac OSX System Configuration for Mac OS X and Windows Systems Registry for Windows. If both lowercase and uppercase environment variables exist (and disagree), lowercase is preferred.
>
> * **[Class]** `Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)`This class is an abstraction of a URL request.
>
>   1. `url`: url should be a string containing a valid URL.
>   2. `data`: must be an object specifying additional data to send to the server, or None if no such data is needed. Currently HTTP requests are the only ones that use data. The supported object types include bytes, file-like objects, and iterables of bytes-like objects. If no Content-Length nor Transfer-Encoding header field has been provided, HTTPHandler will set these headers according to the type of data. Content-Length will be used to send bytes objects, while Transfer-Encoding: chunked as specified in RFC 7230, Section 3.3.1 will be used to send files and other iterables.
>   3. `headers`: headers should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments. This is often used to “spoof” the User-Agent header value, which is used by a browser to identify itself – some HTTP servers only allow requests coming from common browsers as opposed to scripts. For example, Mozilla Firefox may identify itself as "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", while urllib’s default user agent string is "Python-urllib/2.6" (on Python 2.6). An appropriate Content-Type header should be included if the data argument is present. If this header has not been provided and data is not None, Content-Type: application/x-www-form-urlencoded will be added as a default.
>   4. `origin_req_host`: should be the request-host of the origin transaction, as defined by RFC 2965. It defaults to http.cookiejar.request_host(self). This is the host name or IP address of the original request that was initiated by the user. For example, if the request is for an image in an HTML document, this should be the request-host of the request for the page containing the image.
>   5. `unverifiable`: should indicate whether the request is unverifiable, as defined by RFC 2965. It defaults to False. An unverifiable request is one whose URL the user did not have the option to approve. For example, if the request is for an image in an HTML document, and the user had no option to approve the automatic fetching of the image, this should be true.
>   6. `method`: should be a string that indicates the HTTP request method that will be used (e.g. 'HEAD'). If provided, its value is stored in the method attribute and is used by get_method(). The default is 'GET' if data is None or 'POST' otherwise. Subclasses may indicate a different default method by setting the method attribute in the class itself.
>
> * **[Class]** `OpenerDirector`The OpenerDirector class opens URLs via BaseHandlers chained together. It manages the chaining of handlers, and recovery from errors.
> * **[Class]** `BaseHandler`
> * **[Class]** `HTTPDefaultErrorHandler`
> * **[Class]** `HTTPRedirectHandler`
> * **[Class]** `HTTPCookieProcessor`
> * **[Class]** `ProxyHandler`
> * **[Class]** `HTTPPasswordMgr`
> * **[Class]** `HTTPPasswordMgrWithDefaultRealm`
> * **[Class]** `HTTPPasswordMgrWithPriorAuth`
> * **[Class]** `AbstractBasicAuthHandler`
> * **[Class]** `HTTPBasicAuthHandler`
> * **[Class]** `ProxyBasicAuthHandler`
> * **[Class]** `AbstractDigestAuthHandler`
> * **[Class]** `HTTPDigestAuthHandler`
> * **[Class]** `ProxyDigestAuthHandler`
> * **[Class]** `HTTPHandler`
> * **[Class]** `HTTPSHandler`
> * **[Class]** `FileHandler`
> * **[Class]** `DataHandler`
> * **[Class]** `FTPHandler`
> * **[Class]** `CacheFTPHandler`
> * **[Class]** `UnknownHandler`
> * **[Class]** `HTTPErrorProcessor`


```python
import urllib

response = urllib.request.urlopen("https://httpbin.org")
content = response.read().decode('utf-8')
print(content)

data = bytes(urllib.parse.urlencode({'word':"hello"}),encoding='utf-8')
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read())



```