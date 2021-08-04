import smtplib
from email.mime.text import MIMEText 
from email.header import Header

sender ='from@runoob.com'
receivers = ['1914866205@qq.com'] # 接收邮箱

#三个参数   文本内容 文本格式 编码
message=MIMEText('Python邮件发送测试。。。','plain','utf-8')
message['From']=Header('SMTP打卡','utf-8') # 发送者
message['To']=Header('测试','utf-8') # 接收者

subject= 'Python SMTP 邮件测试'
message['Subject']=Header(subject,'utf-8')


try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')
