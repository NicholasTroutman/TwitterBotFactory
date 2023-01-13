from bs4 import BeautifulSoup
from selenium import webdriver
import time
 
# a module which has functions related to time.
# It can be installed using cmd command:
# pip install time, in the same way as pyautogui.
import pyautogui

from selenium import webdriver
PROXY = "178.167.67.233:55443"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("https://www.google.com")