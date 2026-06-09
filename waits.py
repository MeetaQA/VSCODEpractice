from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total = 0
for price in prices:
    total = total + int(price.text)
print(total)
totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert total == totalamount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text())


# What is implicit wait?
#Global timeout to be put on top of the scripts 

