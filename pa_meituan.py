from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

binary=FirefoxBinary("/opt/firefox/firefox")
browser = webdriver.Firefox(firefox_binary=binary)

browser.implicitly_wait(10) #当没有发现要找元素时隐时等待
browser.get("https://wh.meituan.com/")
print(browser.title)

assert u"美团网" in browser.title
try:
    change_city = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "change-city"))
    )
except:
    print("error")
time.sleep(1)
change_city.click()

city_list = browser.find_element_by_link_text(u"重庆")
city_list.click()

btsearch_text = browser.find_element_by_class_name("header-search-input")
btsearch_text.clear()
btsearch_text.send_keys(u"酒店")
btsearch_text.send_keys(Keys.RETURN)


js = "window.scrollTo(0, document.body.scrollHeight);"
browser.execute_script(js)

htm_const = browser.page_source
soup = BeautifulSoup(htm_const, 'html.parser')
infos = soup.find_all(class_="hotel-list-item")
with open("重庆酒店.txt", "a", encoding="utf-8") as f:
    page_num=0
    for info in infos:
        page_num+=1
        f.write("--"*50)
        f.write('\r\n')
        content = info.get_text()
        for line in [ln for ln in content.splitlines() if ln.strip()]:
            f.write(line)
            f.write('\r\n')
print("success")
browser.close()