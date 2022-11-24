import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 负责发送邮件
# 负责构造邮件内容
# QQ邮箱接收服务器 imap.qq.com 993
# QQ邮箱发送服务器 smtp.qq.com 465,587
'''常规流程
1. 创建smtp对象
2. 连接指定服务器
3. 登陆邮箱
4. 发邮件
'''
'''
# 创建smtp对象
smtpObj = smtplib.SMTP('smtp.qq.com', 465, 'localhost')
# 发送邮件
SMTP.sendmail('','',msg)
'''
# 第三方SMTP服务
mail_host = 'smtp.qq.com'
# 服务器主机
mail_user = '*@qq.com'
# 用户
mail_pwd = '*?'
# 密码
sender = 'smtp.qq.com'
receiver = ['*@qq.com']

message = MIMEText('测试邮件', 'plain', 'utf-8')
message['From'] = Header('发件人', 'utf-8')
'''发送者'''
message['To'] = Header('收件人', 'utf-8')
'''接收者'''
subject = '测试邮件主题'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print('邮件已发送')
except smtplib.SMTPException:
    print('发送失败')

## smtp协议没有启用， 没有授权码报错了，
## smtplib.SMTPAuthenticationError: (535, b'Login Fail. Please enter your authorization code to login.