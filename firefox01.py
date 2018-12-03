from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary=FirefoxBinary("/opt/firefox/firefox")
browser = webdriver.Firefox(firefox_binary=binary)
browser.get("http://baidu.com")
print(browser.title)

assert u"百度" in browser.title
elem = browser.find_element_by_name("wd")   #选中name=wd的元素
id_button = browser.find_element_by_id("su")
elem.clear()    #清除输入框内容
elem.send_keys(u"网络爬虫")

# elem.send_keys(Keys.RETURN)
id_button.click()
time.sleep(2)
assert u"网络爬虫" in browser.page_source
aa = browser.find_element_by_xpath("//div[@id='content_left']//a")
print(aa)
aa.click()

time.sleep(3)
browser.close()