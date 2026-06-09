import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#service_obj = Service("C:\SeleniumPythonProject\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#webdriver.chrome(Service=service_obj)

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.quit

