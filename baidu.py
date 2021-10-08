from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"http://www.baidu.com")

driver.maximize_window()

# driver.find_element_by_id("key").send_keys("奥迪")
#
# driver.find_element_by_class_name("iconfont").click()
driver.find_element_by_xpath("//*[@id='kw']").send_keys("坦克300")
driver.find_element_by_xpath("//*[@id='su']").click()
# driver.find_element_by_xpath(("//*[@class='wbrjf67']")).click()
# driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
# driver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n7/jfs/t1/205226/20/9809/112872/615e991fE2cecdd41/db42acdbae68b709.jpg']").click()