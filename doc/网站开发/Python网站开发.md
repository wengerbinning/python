# Python网站开发


* CS(Client/Server):
* BS(Browser/Server,浏览器与服务器):

## Web 开发历程

1. 静态Web页面
2. CGI(Common Gateway Interface,C/C++编写):
3. ASP/JSP/PHP:ASP是微软,JSP使用Java,PHP本身是开源脚本;
4. MVC(Model-View-Controller):
5. 异步开发:
6. MVVM:

## HTTP协议简介

* HTTP(,超文本传输协议):

## WSGI接口

* WSGI(Web Server Gateway Interface,网页服务获取接口);
* application(environ, start_response)

  ```python
  def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
  ```

### wsgiref 模块

* Python内置的一个WSGI服务器;
  
  ```python
  # server.py
    # 从wsgiref模块导入:
    from wsgiref.simple_server import make_server
    # 导入我们自己编写的application函数:
    from hello import application

    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
  ```

## Web 框架
* 123;
### Flask 框架:
* 安装框架,Flask支持的模板是jinja2;
  ```
  pip install Flask
  ```
* 处理3个URL:
  ```
  from flask import Flask
    from flask import request

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        return '<h1>Home</h1>'

    @app.route('/signin', methods=['GET'])
    def signin_form():
        return '''<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
                </form>'''

    @app.route('/signin', methods=['POST'])
    def signin():
        # 需要从request对象读取表单内容：
        if request.form['username']=='admin' and request.form['password']=='password':
            return '<h3>Hello, admin!</h3>'
        return '<h3>Bad username or password.</h3>'

    if __name__ == '__main__':
        app.run()
  ```
* 通过render_template()实现模板渲染:
  ```
  from flask import Flask, request, render_template

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        return render_template('home.html')

    @app.route('/signin', methods=['GET'])
    def signin_form():
        return render_template('form.html')

    @app.route('/signin', methods=['POST'])
    def signin():
        username = request.form['username']
        password = request.form['password']
        if username=='admin' and password=='password':
            return render_template('signin-ok.html', username=username)
        return render_template('form.html', message='Bad username or password', username=username)

    if __name__ == '__main__':
        app.run()
  ```
* 编写jinja2模板,将模板放在templates文件夹中放在程序同目录下;
  ```
  # home.html
  <html>
    <head>
    <title>Home</title>
    </head>
    <body>
    <h1 style="font-style:italic">Home</h1>
    </body>
    </html>

  # form.html
  <html>
    <head>
    <title>Please Sign In</title>
    </head>
    <body>
    {% if message %}
    <p style="color:red">{{ message }}</p>
    {% endif %}
    <form action="/signin" method="post">
        <legend>Please sign in:</legend>
        <p><input name="username" placeholder="Username" value="{{ username }}"></p>
        <p><input name="password" placeholder="Password" type="password"></p>
        <p><button type="submit">Sign In</button></p>
    </form>
    </body>
    </html>
  # signin-ok.html
  <html>
    <head>
    <title>Welcome, {{ username }}</title>
    </head>
    <body>
    <p>Welcome, {{ username }}!</p>
    </body>
    </html>
  ```

### Django 框架
* 全能型Web框架;

### web.py 框架
* 一个小巧的Web框架;

### Bottle 框架
* 与Flask类似的Web框架;

### Tornado 框架
* Facebook的开源异步Web框架;

## 模板
* MVC(Model-View-Controller,模型-视图-控制器):
  1. Model:模板;
  2. View: 负责显示逻辑,替换模板中的变量;
  3. Controller:Python处理URL的函数,负责业务逻辑;
* 常用模板有jinja2、Mako、cheetah、Django; 


