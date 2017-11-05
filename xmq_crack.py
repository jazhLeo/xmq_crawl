#!/usr/bin/env python 
# -*- coding=UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


driver = webdriver.Chrome()
driver.get('https://wx.xiaomiquan.com/dweb/')

# 扫码等待
while 'index' not in driver.current_url:
    sleep(1)
print 'jump done'

# 定位圈子：安全技能树
elem = driver.find_elements_by_xpath('//*[@id="leftgroup"]/div[1]/div/ul/li')
for el in elem:
    if el.text == u'安全技能树':
        el.click()
        print 'i found it'

# 等待页面加载完毕
driver.implicitly_wait(30)

# 定位筛选按钮
sx_but = driver.find_element_by_xpath('/html/body/xmq-web/xmq-index/div/div[1]/div[1]/div/xmq-topic/div[1]/div/ul/div/div/p/span')
sx_but.click()

#定位精华按钮
jh_but = driver.find_element_by_xpath('/html/body/xmq-web/xmq-index/div/div[1]/div[1]/div/xmq-topic/div[1]/div/ul/div/div/div/ul/li[2]')
jh_but.click()