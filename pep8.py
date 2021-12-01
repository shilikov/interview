
import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart



class Email:
    def __init__(self, login, password):
        self.login = f'{login}@gmail.com'
        self.password = password


    def send_message(self, server, port, recipients, subject, message):
        send_email_message = MIMEMultipart()
        send_email_message['From'] = self.login
        send_email_message['To'] = ', '.join(recipients)
        send_email_message['Subject'] = subject
        send_email_message.attach(MIMEText(message))
        send_mail = smtplib.SMTP(server, port)
        send_mail.ehlo()
        send_mail.starttls()
        send_mail.ehlo()
        send_mail.login(self.login, self.password)
        result = send_mail.sendmail(self.login, send_mail, send_email_message.as_string())
        send_mail.quit()
        return result


    def recieve(self, server, mailbox_, header=None):
        recieve_mail = imaplib.IMAP4_SSL(server)
        recieve_mail.login(self.login, self.password)
        recieve_mail.list()
        recieve_mail.select(mailbox=mailbox_)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = recieve_mail.uid('search', header, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = recieve_mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        recieve_email_message = email.message_from_string(raw_email)
        recieve_mail.logout()
        return recieve_email_message

if __name__ == '__main__':
    gmail = Email('login@gmail.ru', 'qwerty')
    print(gmail.send_message(
        'smtp.gmail.com',
        587,
        ['vasya@email.com', 'petya@email.com'],
        'Test message',
        'Body of test message'
    ))
    print(gmail.recieve('imap.gmail.com', 'inbox'))




