#!/usr/bin/env python 
# -*-coding=UTF8-*-
# import requests
from selenium import webdriver
# from time import *
# from PIL import Image
# from io import BytesIO

driver = webdriver.Chrome()
driver.get("https://wx.xiaomiquan.com/dweb/")
# driver.switch_to_frame("nlogin_iframe")
# elem = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/img')
# img_url = elem.get_attribute('src')
# img_res = requests.get(img_url)

# img = Image.open(BytesIO(img_res.content))

# img.show()
print driver.current_url
# print elem
driver.close()