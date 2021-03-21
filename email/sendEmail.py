#!usr/bin python
# -*- coding: utf-8 -*-

__author__ = "ClarkAaron"

'''
电子邮件的演示模块(发送邮件):
    0. 创建server对象:使用smtplib的SMTP建立;
    1. 登录邮件服务器:使用login(user, password)登录;
    2. 编辑文本内容并发送:使用sendmail(from_addr,[to_addr],message)发送内容;


'''
import smtplib
#from email.message import EmailMessage
from email.mime.text import MIMEText

title = "Demo_Send_Email"
content = "This is a demo program,testing a send email!"
# 创建Emailmessage对象以及邮件内容;
message = MIMEText(content)
#message.set_content( content )
message['Subject'] = title
#设置主要参数
from_addr = "clarkaaron@163.com"
password = "2803611373zwb"
to_addr0 = "clarkaaron@qq.com"
to_addr1 = "clack3014@163.com"
smtp_server = "smtp.163.com"

message['From'] = from_addr
message['To'] = to_addr0
print('-'*10)
print(message)
print('-'*10)
#连接SMTP服务器
server = smtplib.SMTP(smtp_server, 25)
#开启调式功能
server.set_debuglevel(1)
#验证登录
try:
    status = server.login(from_addr,password)
    print("登录成功:{}".format(status[0]) )
except:
    print("账号或密码错误!")

#发送邮件
status = server.sendmail(from_addr,[to_addr0,],message.as_string() )
print(status)
#退出服务
#server.quit()

