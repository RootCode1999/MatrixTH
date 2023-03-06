import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'
mail_user = '邮箱地址'
mail_pass = ''
sender = '邮箱地址'
receivers = []


def sendmail(content='Hello', receiver=['邮箱地址']):
    try:
        res = {}
        receivers = receiver
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = 'MatrixTH'
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        return "success"
    except smtplib.SMTPException as e:
        error = {}
        return str(e)
