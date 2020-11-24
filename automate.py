from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json


from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

driver.maximize_window()
user_elem = driver.find_element_by_name("session_key")
print(user_elem.is_displayed())
print(user_elem.is_enabled())

pwd_elem = driver.find_element_by_name("session_password")
print(pwd_elem.is_displayed())
print(pwd_elem.is_enabled())

user_elem.send_keys("") #usn

pwd_elem.send_keys("")  # pwd






pwd_elem.submit()

driver.find_element_by_id("ember26").click()   # clicks on jobs icon

driver.find_element(By.ID,"jobs-search-box-location-id-ember991").send_keys("Bangalore")