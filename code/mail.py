from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    MAIL_USERNAME = 'han_yin9@163.com',
    MAIL_PASSWORD = 'yinhan4321',)

mail = Mail(app)

@app.route('/')
def index():
 # sender 发送方，recipients 接收方列表
    msg = Message("This is title",sender='han_yin9@163.com', recipients=['han_yin9@163.com','han_yin9@126.com'])
    #邮件内容
    msg.body = "Flask test mail"
    #发送邮件
    mail.send(msg)
    print("Mail sent")
    return "Sent　Succeed"

if __name__ == "__main__":
    app.run()