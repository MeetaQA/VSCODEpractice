from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
actions = ActionChains(driver)
#actions.move_to_element()
#actions.context_click()
#actions.drag_and_drop()
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
