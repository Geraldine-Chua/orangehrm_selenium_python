from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
element = driver.find_element_by_id("txtUsername")
element.send_keys("Admin")
element = driver.find_element_by_id("txtPassword")
element.send_keys("admin123")
element.send_keys(Keys.RETURN)
element = driver.find_element_by_id("menu_pim_viewMyDetails")
element.click()
element = driver.find_element_by_id("btnAddAttachment")
element.click()
element = driver.find_element_by_id("ufile").send_keys("/Users/ritchieroi/Documents/tulips.jpg")
time.sleep(3)
element = driver.find_element_by_id("txtAttDesc")
element.send_keys("this is my favorite flower :) ")
element = driver.find_element_by_id("btnSaveAttachment")
element.click()
