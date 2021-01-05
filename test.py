
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def test():
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    sender = '774135735@qq.com'
    password = 'hzkfvlxnaugxbfic'
    qqmail.login(sender, password)
    receiver = ['xs@tofsq.com', '1914297430@qq.com', '317846732@qq.com']

    content = '网页重新上线'
    message = MIMEText(content, 'plain', 'utf-8')
    subjuet = '报警'
    message['Subject'] = Header(subjuet, 'utf-8')
    try:
        qqmail.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except:
        print('邮件发送失败')
    qqmail.quit()
if __name__ == '__main__':
    test()
