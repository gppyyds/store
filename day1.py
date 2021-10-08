# import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"http://www.jd.com")

driver.maximize_window()

# driver.find_element_by_id("key").send_keys("奥迪")
#
# driver.find_element_by_class_name("iconfont").click()
driver.find_element_by_xpath("//*[@id='key']").send_keys("ipone 13 pro")
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
driver.find_element_by_xpath("//*[@class='p-img']").click()
# time.sleep()

# driver.quit()