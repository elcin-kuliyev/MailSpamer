from smtplib import SMTP_SSL
from email.MIMEText import MIMEText

def sendMail(client_mail, message, header):
    my_donor_mail="..."                                                 # адрес электронной почты источника рассылки
    msg = MIMEText(message, "html", "utf-8")
    msg['Subject'] = header
    msg['From'] = my_donor_mail
    msg['To'] = client_mail
    smtp = SMTP_SSL()
    smtp.connect('smtp.yandex.ru')
    smtp.login(my_donor_mail, '...')                    # пароль почты
    smtp.sendmail(my_donor_mail, client_mail, msg.as_string())
    smtp.quit()

mail_list='list.txt'                                                                 # файл со списком адресов рассылки: один адрес - одна строка
mail_body='...'                                                                 # файл с текстом письма
header='...'                                                                    # заголовок письма

f=open(mail_body, 'r')
message=f.read()
f.close()

for mail in open(mail_list, 'r'):
    try:
        sendMail(mail, message, header)
        print 'Send to: '+mail[:-1]
    except:
        print 'NOT send to: '+mail[:-1]

f.close()