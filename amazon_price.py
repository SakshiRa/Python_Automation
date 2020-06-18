#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 07:38:07 2020

@author: sakshirathi
"""

import requests
from bs4 import BeautifulSoup

import smtplib
import time


URL = 'https://www.amazon.com/gp/product/B01HXHVMHC?pf_rd_r=3EDFZGWX5MB339NTGR3R&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:77.0) Gecko/20100101 Firefox/77.0 '}

def check_price():
    

    page = requests.get(URL, headers = headers)
    
    soup = BeautifulSoup(page.content , 'html.parser')
        
    price = soup.find(id = "priceblock_ourprice").get_text()
    
    converted_price = float(price[1:])
    
    
    if (converted_price < 30.00):
        send_mail()
    
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('XYZ','XYZ')
    
    subject = 'Price fell donw!'
    body = 'check the amazon link https://www.amazon.com/gp/product/B01HXHVMHC?pf_rd_r=3EDFZGWX5MB339NTGR3R&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee'
    msg = f"subject:{subject}\n\n{body}"
    
    server.sendmail('XYZ', 'XYZ', msg)
    
    print('Hey email has been send!')
    
    server.quit()
    

while(True):
    check_price()
    time.sleep(3600)
