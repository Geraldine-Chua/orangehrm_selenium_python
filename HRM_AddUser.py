from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
print("start of program")


#print("Enter User Name")
#user_name = str(input())
user_name = "Admin"
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
element = driver.find_element_by_id("txtUsername")
element.send_keys(user_name)
element = driver.find_element_by_id("txtPassword")
element.send_keys("admin123")
element.send_keys(Keys.RETURN)
element = driver.find_element_by_id("menu_admin_viewAdminModule")
element.click()
element = driver.find_element_by_id("btnAdd")
element.click()
element = Select(driver.find_element_by_id("systemUser_userType"))
element.select_by_visible_text("Admin")
element = driver.find_element_by_id("systemUser_employeeName_empName")
element.send_keys("John Smith")
element = driver.find_element_by_id("systemUser_userName")
element.send_keys("JohnSmith3")
element = Select(driver.find_element_by_id("systemUser_status"))
element.select_by_visible_text("Enabled")
element = driver.find_element_by_id("systemUser_password")
element.send_keys("HelloFr!d@y123wQ")
element = driver.find_element_by_id("systemUser_confirmPassword")
element.send_keys("HelloFr!d@y123wQ")
element = driver.find_element_by_id("btnSave")
element.click()




