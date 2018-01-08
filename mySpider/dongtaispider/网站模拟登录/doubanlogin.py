# coding=utf8
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001")
time.sleep(3)

#输入帐号密码
driver.find_element_by_name("form_email").send_keys("18861816083")
driver.find_element_by_name("form_password").send_keys("320316www")

#模拟点击登录
driver.find_elements_by_class_name("btn-submit")[0].click()

#等待3s

#生成登录后的快照
driver.save_screenshot("douban.png")

with open("douban.html","w") as file:
    file.write(driver.page_source.replace(u'\xa9', u''))

driver.quit()