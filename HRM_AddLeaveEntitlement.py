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
element = driver.find_element_by_id("menu_leave_viewLeaveModule")
element.click()
element = driver.find_element_by_id("menu_leave_Entitlements")
element.click()
element = driver.find_element_by_id("menu_leave_addLeaveEntitlement")
element.click()
time.sleep(3)
element = driver.find_element_by_id("entitlements_employee_empName")
element.send_keys("John Smith")
element.send_keys(Keys.RETURN)
time.sleep(4)
element = Select(driver.find_element_by_id("entitlements_leave_type"))
element.select_by_visible_text("US - Vacation")
element = Select(driver.find_element_by_id("period"))
element.select_by_visible_text("2021-01-01 - 2021-12-31")
element = driver.find_element_by_id("entitlements_entitlement")
element.send_keys("30")
element = driver.find_element_by_id("btnSave")
element.click()

