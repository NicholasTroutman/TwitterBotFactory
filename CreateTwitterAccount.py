from bs4 import BeautifulSoup
from selenium import webdriver
from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup as bs
from lxml import etree, html
import sys, os
from io import StringIO
from xml.dom.minidom import parse, parseString 
import pandas as pd
import time
import requests
import re
import random
import pyautogui as pag
import json
from pywinauto import application
    

for i in range(0,10):
    
    #pag.moveTo(1200,1075,duration=0.5)
    #pag.click()
    #pag.moveTo(270,250,duration=0.5)
    #pag.click()
    #time.sleep(3)
    
    #pag.moveTo(340,750,duration=0.5)
    #pag.click()
    #time.sleep(15)
                                        
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    url = "https://twitter.com/i/flow/signup"
    driver.get(url)
    html=driver.page_source #includes text
    
     
    # a module which has functions related to time.
    # It can be installed using cmd command:
    # pip install time, in the same way as pyautogui.
   
    #getEmailAddress
    emailurl="https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    
    
    emails= requests.post(emailurl)
    
                                        
    
    email=emails.text[2:-2]
    name=email.split('@')[0]
    domain=email.split('@')[1]
    
     
    # makes program execution pause for 10 sec
    time.sleep(5)   
    pag.moveTo(500, 500, duration = 0.7)
    pag.click()
    pag.write('NickTsBiggestFan#'+str(int(random.random()*10000))) 
    
     
    pag.moveTo(500,700,duration=0.7)
    pag.click()
    
    
    pag.moveTo(500,600,duration=0.7)
    pag.click()
    pag.write(email)  
    
    pag.press('tab')
    pag.press('tab')
    pag.write('a')
    pag.press('tab')
    pag.write('12')
    pag.press('tab')
    pag.write('1992')
    time.sleep(2)
    pag.press('tab')
    pag.press('Enter')
    
    pag.moveTo(1200,500,duration=0.7)
    pag.click()
    pag.press('tab')
    pag.press('tab')
    time.sleep(1)
    pag.press('Enter')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    time.sleep(1)
    pag.press('Enter')
    #WRITE Vcode
    
    mailboxurl="https://www.1secmail.com/api/v1/?action=getMessages&login="+name+"&domain="+domain
    Data={
    	"action": "getMessages",
    	"login": name,
    	"domain": domain}
    
    time.sleep(6)
    mailbox=requests.get(mailboxurl,Data).text
    
    vcode=re.findall(r"\D(\d{6})\s", mailbox)[0]
    
    pag.moveTo(500, 500, duration = 0.7)
    pag.click()
    pag.write(vcode) 
    time.sleep(1)
    pag.press('tab')
    pag.press('tab')
    pag.press('Enter')
                                        
    time.sleep(1)
    
    pag.write('Boosting01')
    time.sleep(1.2)
    pag.press('Enter')
    time.sleep(4)
    
    nickUrl="https://twitter.com/troutmanick"
    pag.moveTo(400,100)
    pag.click()
    pag.write("https://twitter.com/home")
    pag.press('Enter')
    
    pag.moveTo(1200,250,duration=0.7)
    time.sleep(8)
    pag.click()
    
    pag.write("troutmanick")
    pag.moveTo(1200,400,duration=0.3)
    time.sleep(3)
    pag.click()
    
    time.sleep(4)
    pag.moveTo(975,620)
    pag.click()
    time.sleep(2)
    
    
    driver.quit()
    print(i)