from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://dev.savoya.net/")
driver.maximize_window()
driver.find_element(By.ID, "email").send_keys("david.savoya+users24773@gmail.com")
driver.find_element(By.ID, "password").send_keys("canteen total palatine buffer")
driver.find_element(By.CSS_SELECTOR, "#btn-login").click()
wait = WebDriverWait(driver,10)
wait.until(EC.url_contains("https://dev.savoya.net/savoya/dashboard"))
