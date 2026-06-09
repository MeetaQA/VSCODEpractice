from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client/")
#Linktext
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("pawarmeeta29@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("12345")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

# in xpath we give slash whereas in css we just give the space 
#xpath = //form/div[2]/input
#Css = form div:nth-child(2) input
# based on the button text also xpath can be generated but not the css selector 
# ///button[@text()='save password'], but can not create a CSS from that.





