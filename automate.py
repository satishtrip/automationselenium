from selenium import webdriver

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver")
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.implicitly_wait(1000)
driver.close()