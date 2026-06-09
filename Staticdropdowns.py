from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#there is a class "select" in selenium
#Dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#Dropdown.select_by_visible_text("Female")
#Dropdown.select_by_index(0)
#Dropdown.select_by_value

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
Dropdown1 = Select(driver.find_element(By.TAG_NAME  , "select"))
Dropdown1.select_by_index(0)


