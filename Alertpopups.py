from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "meeta"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alertext = alert.text   
print(alertext)
alert.accept()
assert name in alertext
#alert.dismiss()