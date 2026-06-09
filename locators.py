import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#service_obj = Service("C:\SeleniumPythonProject\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#webdriver.chrome(Service=service_obj)

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# ID, xpath, CSSselector, linktext, name, classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Meeta")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("122345")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()

# xpath = //tagname[@attribute.value]
#Cssselector = tagname[attribute.value]
#ID = Validcss, .classname =valid CSS
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success12" in message





