#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
#将浏览器最大化显示
browser.maximize_window()
time.sleep(3)
#设置浏览器的宽为800和高为1800
browser.set_window_size(800, 1800)
time.sleep(3)
#操作浏览器的前进和后退
#访问百度首页
first_url= 'http://www.baidu.com'
browser.get(first_url)
time.sleep(2)
#访问新闻页面
second_url='http://news.baidu.com'
browser.get(second_url)
time.sleep(2)
#返回（后退）到百度首页
browser.back()
#控制浏览器的滚动条
#搜索
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
browser.execute_script(js)
time.sleep(3)
browser.quit()