#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome()
browser.get("http://news.baidu.com")
qqq =browser.find_element_by_xpath(".//*[@id='s_btn_wr']")
ActionChains(browser).context_click(qqq).perform() #右键
ActionChains(browser).double_click(qqq).perform() #双击
#定位元素的原位置
element = browser.find_element_by_id("s_btn_wr")
#定位元素要移动到的目标位置
target = browser.find_element_by_class_name("btn")
#执行元素的移动操作
ActionChains(browser).drag_and_drop(element, target).perform()
