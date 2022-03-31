from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

username = input("enter the username: ")
password = input("enter the password: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")

driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(2)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
time.sleep(2)
driver.find_element_by_class_name("L3NKy").send_keys(Keys.ENTER)
time.sleep(20)
driver.close()
print("test closed")