# -*- coding:utf-8 -*-
from threading import Thread
from flask_mail import Message,Mail
from flask import render_template,Flask
from flask import current_app    # 这样就不用使用from manager import app
import os


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '12345678@qq.com' #这里需要更改成自己的
app.config['MAIL_PASSWORD'] = 'otkoyseobndjeadb'#这里需要更改成自己的

mail = Mail(app)

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


# 四个参数分别为(1.接收者邮箱地址 2.主题 3.模板 4.可变参数)
def send_email(to, subject, template, **kwargs):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    # msg.body = 'text body'
    # msg.html = '<b>HTML</b> body'
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr