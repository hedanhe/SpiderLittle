from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary=FirefoxBinary("/opt/firefox/firefox")
browser = webdriver.Firefox(firefox_binary=binary)
browser.get("https://passport.csdn.net/passport_fe/login.html")
print(browser.title)

assert u"CSDN" in browser.title
btn_login_mode = browser.find_element_by_xpath("//li[@class='text-tab border-right']/a")
btn_login_mode.click()


username = browser.find_element_by_id("all")
password = browser.find_element_by_id("password-number")

username.clear()
password.clear()

username.send_keys(u"17671011776")
password.send_keys(u"mm520131400")
time.sleep(0.5)
# login_btn = browser.find_elements_by_partial_link_text(u"登录")
# login_btn.click()
password.send_keys(Keys.RETURN)
time.sleep(2)

browser.close()