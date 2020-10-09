#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)
# 通过id定位到输入框以后，模拟键盘输入“test”
driver.find_element_by_id("kw").send_keys("test")
time.sleep(2)
#通过id定位到输入框以后，清空输入框的内容
driver.find_element_by_id("kw").clear()
# 通过id定位到输入框以后，模拟键盘输入“selenium”
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)
#通过submit() 来代替click
driver.find_element_by_id("su").submit()
time.sleep(3)
#通过text获取id = cp 元素的文本信息
data=driver.find_element_by_id("wrapper").text
print(data) #打印信息
time.sleep(3)
driver.quit()