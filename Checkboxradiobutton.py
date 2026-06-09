from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
   if checkbox.get_attribute("value") =="option2":
      checkbox.click()
      #assert checkbox.is_selected()
      break
   

Radios = driver.find_elements(By.XPATH, "//input[@type='radio']") 

for radio in Radios:
   if radio.get_attribute("value") == "radio3":
      radio.click()
      break
   
statisdropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
statisdropdown.select_by_index(1)
