# coding=utf8
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001")
time.sleep(3)

#输入帐号密码
driver.find_element_by_name("form_email").send_keys("1140377034@qq.com")
driver.find_element_by_name("form_password").send_keys("320316www")

#模拟点击登录
driver.find_element_by_xpath("//input[@class='bn_submit']").click()

#等待3s

#生成登录后的快照
driver.save_screenshot("douban.png")

with open("douban.html","w") as file:
    file.write(driver.page_source)

driver.quit()