# -*- coding: utf-8 -*-

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("maximize_window")
driver.maximize_window() #������������ʾ
driver.find_element_by_xpath("//*[@id='kw']").send_keys("China")
time.sleep(3)
driver.quit()