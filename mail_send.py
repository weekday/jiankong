#coding:utf-8

import smtplib
from diff_file import betweenDiff
from email.mime.text import MIMEText

mail_user = 'xxxxxxxx@qq.com'
mail_pass = 'nsqfcdmatzdhbjbe'
mail_server = 'smtp.qq.com'
mail_port = 465
to_user = 'xxxxxx@rongchat.com'

def send_mail(title,content):
    #创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content,_subtype = 'html',_charset = 'utf-8')
    msg['Subject'] = title
    msg['From'] = mail_user
    msg['To'] = to_user
    try:
        #登录smtp服务器
        server = smtplib.SMTP_SSL(mail_server,mail_port)
        server.login(mail_user,mail_pass)
        #邮件发送
        server.sendmail(mail_user,to_user,msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':
    monitor_files = '/root/PythonProjects/jiankong/test.txt'
    old_file = '/root/PythonProjects/jiankong/test1.txt'
    content = betweenDiff(old_file,monitor_files)
    title = 'This is html file'
    send_mail(title,content)