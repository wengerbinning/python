# URLLIB

[//]: # (__author__ = "Clark Aaron")
[//]: # (__version__ = "v0.0")

urllib is a package that collects several modules for working with URLs. It include `request`, `parse`, `error`, `robotparser` and `response`  module.

## request Module

request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

### Class

* `Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)`This class is an abstraction of a URL request.

  * **[Public attribute]** 
  
  > * `full_url`: The original URL passed to the constructor. 
  > * `type`: The URI scheme.
  > * `host`: The URI authority, typically a host, but may also contain a port separated by a colon.
  > * `origin_req_host`: The original host for the request, without port.
  > * `selector`: The URI path. If the Request uses a proxy, then selector will be the full URL that is passed to the proxy.
  > * `data`: The entity body for the request, or None if not specified.
  > * `unverifiable`: boolean, indicates whether the request is unverifiable as defined by RFC 2965.
  > * `method`: The HTTP request method to use. By default its value is None, which means that get_method() will do its normal computation of the method to be used. Its value can be set (thus overriding the default computation in get_method()) either by providing a default value by setting it at the class level in a Request subclass, or by passing a value in to the Request constructor via the method argument.

  * **[Public method]**
  
  > * `__init__()`: 
  >
  >> 1. `url`: url should be a string containing a valid URL.
  >> 2. `data`: must be an object specifying additional data to send to the server, or None if no such data is needed. Currently HTTP requests are the only ones that use data. The supported object types include bytes, file-like objects, and iterables of bytes-like objects. If no Content-Length nor Transfer-Encoding header field has been provided, HTTPHandler will set these headers according to the type of data. Content-Length will be used to send bytes objects, while Transfer-Encoding: chunked as specified in RFC 7230, Section 3.3.1 will be used to send files and other iterables.
  >> 3. `headers`: headers should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments. This is often used to “spoof” the User-Agent header value, which is used by a browser to identify itself – some HTTP servers only allow requests coming from common browsers as opposed to scripts. For example, Mozilla Firefox may identify itself as "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", while urllib’s default user agent string is "Python-urllib/2.6" (on Python 2.6). An appropriate Content-Type header should be included if the data argument is present. If this header has not been provided and data is not None, Content-Type: application/x-www-form-urlencoded will be added as a default.
  >> 4. `origin_req_host`: should be the request-host of the origin transaction, as defined by RFC 2965. It defaults to http.cookiejar.request_host(self). This is the host name or IP address of the original request that was initiated by the user. For example, if the request is for an image in an HTML document, this should be the request-host of the request for the page containing the image.
  >> 5. `unverifiable`: should indicate whether the request is unverifiable, as defined by RFC 2965. It defaults to False. An unverifiable request is one whose URL the user did not have the option to approve. For example, if the request is for an image in an HTML document, and the user had no option to approve the automatic fetching of the image, this should be true.
  >> 6. `method`: should be a string that indicates the HTTP request method that will be used (e.g. 'HEAD'). If provided, its value is stored in the method attribute and is used by get_method(). The default is 'GET' if data is None or 'POST' otherwise. Subclasses may indicate a different default method by setting the method attribute in the class itself.

  > * `get_method()`: Return a string indicating the HTTP request method. If Request.method is not None, return its value, otherwise return 'GET' if Request.data is None, or 'POST' if it’s not. This is only meaningful for HTTP requests.
  > * `add_header(key, val))`: Add another header to the request. Headers are currently ignored by all handlers except HTTP handlers, where they are added to the list of headers sent to the server. Note that there cannot be more than one header with the same name, and later calls will overwrite previous calls in case the key collides. Currently, this is no loss of HTTP functionality, since all headers which have meaning when used more than once have a (header-specific) way of gaining the same functionality using only one header.
  > * `add_unredirected_header(key, header)`: Add a header that will not be added to a redirected request.
  > * `has_header(header)`: Return whether the instance has the named header (checks both regular and unredirected).
  > * `remove_header(header)`: Remove named header from the request instance (both from regular and unredirected headers).
  > * `get_full_url()`: Return the URL given in the constructor.
  > * `set_proxy(host, type)`: Prepare the request by connecting to a proxy server. The host and type will replace those of the instance, and the instance’s selector will be the original URL given in the constructor.
  > * `get_header(header_name, default=None)`: Return the value of the given header. If the header is not present, return the default value.
  > * `header_items()`: Return a list of tuples (header_name, header_value) of the Request headers.

* `OpenerDirector`The OpenerDirector class opens URLs via BaseHandlers chained together. It manages the chaining of handlers, and recovery from errors.
* `BaseHandler`
* `HTTPDefaultErrorHandler`
* `HTTPRedirectHandler`
* `HTTPCookieProcessor`
* `ProxyHandler`
* `HTTPPasswordMgr`
* `HTTPPasswordMgrWithDefaultRealm`
* `HTTPPasswordMgrWithPriorAuth`
* `AbstractBasicAuthHandler`
* `HTTPBasicAuthHandler`
* `ProxyBasicAuthHandler`
* `AbstractDigestAuthHandler`
* `HTTPDigestAuthHandler`
* `ProxyDigestAuthHandler`
* `HTTPHandler`
* `HTTPSHandler`
* `FileHandler`
* `DataHandler`
* `FTPHandler`
* `CacheFTPHandler`
* `UnknownHandler`
* `HTTPErrorProcessor`

### Function

* `urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)`Open the URL url, which can be either a string or a Request object.

  > 1. `url`: can be either a string or a Request object.
  > 2. `data`: must be an object specifying additional data to be sent to the server, or None if no such data is needed. See Request for details.
  > 3. `timeout`: The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). This actually only works for HTTP, HTTPS and FTP connections.
  > 4. `cafile`: cafile should point to a single file containing a bundle of CA certificates.
  > 5. `capath`: capath should point to a directory of hashed certificate files.
    
  > Deprecated since version 3.6: cafile, capath and cadefault are deprecated in favor of context. Please use ssl.SSLContext.load_cert_chain() instead, or let ssl.create_default_context() select the system’s trusted CA certificates for you.
 
* `install_opener(opener)`: Install an OpenerDirector instance as the default global opener. Installing an opener is only necessary if you want urlopen to use that opener; otherwise, simply call OpenerDirector.open() instead of urlopen(). The code does not check for a real OpenerDirector, and any class with the appropriate interface will work.
 
* `build_opener([handler, ...])`Return an OpenerDirector instance, which chains the handlers in the order given. handlers can be either instances of BaseHandler, or subclasses of BaseHandler (in which case it must be possible to call the constructor without any parameters). Instances of the following classes will be in front of the handlers, unless the handlers contain them, instances of them or subclasses of them: ProxyHandler (if proxy settings are detected), UnknownHandler, HTTPHandler, HTTPDefaultErrorHandler, HTTPRedirectHandler, FTPHandler, FileHandler, HTTPErrorProcessor.

* `pathname2url(path)`Convert the pathname path from the local syntax for a path to the form used in the path component of a URL. This does not produce a complete URL. The return value will already be quoted using the quote() function.

* `url2pathname(path)`Convert the path component path from a percent-encoded URL to the local syntax for a path. This does not accept a complete URL. This function uses unquote() to decode path.
 
* `getproxies()`This helper function returns a dictionary of scheme to proxy server URL mappings. It scans the environment for variables named <scheme>_proxy, in a case insensitive approach, for all operating systems first, and when it cannot find it, looks for proxy information from Mac OSX System Configuration for Mac OS X and Windows Systems Registry for Windows. If both lowercase and uppercase environment variables exist (and disagree), lowercase is preferred.



## parse Module

parse module defines a standard interface to break URL strings up in components (addressing scheme, network location, path etc.), to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL”. This module has been designed to match the Internet RFC on Relative Uniform Resource Locators. It supports the following URL schemes: file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp, shttp, sip, sips, snews, svn, svn+ssh, telnet, wais, ws, wss. And defines functions that fall into two broad categories: URL parsing and URL quoting. These are covered in detail in the following sections.

### URL parsing

#### Class
#### Function


### URL quoting

#### Function

## error Module

error module defines the exception classes for exceptions raised by urllib.request. The base exception class is URLError.

## robotparser Module

## response Module


## Example

* **[Deafult]** demo request data. 

```python
from urllib import request

URL = "http://www.baidu.com"

response = request.urlopen(URL)

print(response.url)
print(response.getcode())
print(response.status)
content = response.read(300)
print(content.decode('utf-8'))
```

* **[Headers]** demo request data with headers.

```python
from urllib import request

URL = "http://www.baidu.com"

url = request.Request(URL)
url.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

response = request.urlopen(url)
print(response.url)
print(response.getcode())
print(response.status)
content = response.read(300)
print(content.decode('utf-8'))
```