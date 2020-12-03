#make sure to turn on less secure app access for this to work!!
# Takes input url and product id then updates you when the price falls
# below a certain threshhold

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Apple-iPhone-11-128GB-PRODUCT/dp/B07XRPL4CF/ref=sr_1_3?dchild=1&keywords=iphone+12&qid=1598800796&sr=8-3'
headers = {"user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser') #grabs all info about page

    title = soup.find(id="productTitle").get_text().strip() #grabs title of product
    price = soup.find(id="priceblock_ourprice").get_text() #grabs price of product
    converted_price = float(price[+1:]) #only keep price figures

    #if price is less than £740 send email alert
    if(converted_price < 740): 
        send_mail(price)

    print(title)
    print(converted_price)

#sends the email
def send_mail(price):
    # formatting protocol
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #login part
    server.login(#input email , #input password)
    subject = ('price fell to: ' + price[+1:])
    body = 'check: https://www.amazon.co.uk/Apple-iPhone-11-128GB-PRODUCT/dp/B07XRPL4CF/ref=sr_1_3?dchild=1&keywords=iphone+12&qid=1598800796&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    #send email from reece... to reece...
    server.sendmail(
        'email@gmail.com',
        'email@.com',
        msg
    )
    print('Email has been sent')

    server.quit()
while(True):
    check_price()
    time.sleep(60*60*60) # sleeps for a day and checks again
