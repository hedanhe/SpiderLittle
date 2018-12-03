from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://baidu.com")
print(driver.title)

assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫" not in driver.page_source
print(driver.title)
driver.close()