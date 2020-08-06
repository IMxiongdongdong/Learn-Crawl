import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path='D:\Anaconda3\envs\pythonlearn\Scripts\geckodriver.exe')  # selenium3需要指定geckodriver路径
driver.get("http://www.baidu.com")  #  打开百度搜索页面
driver.find_element_by_id("kw").clear() # 清除百度搜索框中内容， kw是百度搜索页面html标签的id
driver.find_element_by_id("kw").send_keys("Python") #  往百度搜索框中添加Python搜索关键字
driver.find_element_by_id("su").click() #找到百度一下按钮，并点击(会执行搜索)， su为搜索按钮的id(可以通过鼠标挪动到百度一下按钮上，右键、选择查看元素，可以看到该button的id名称为su)
time.sleep(5)   #  如果不注释下面那行，需要休眠一定时间才能看到搜索结果，不然会闪现，注释掉的话，该行可以不要
driver.quit() #  关闭浏览器操作