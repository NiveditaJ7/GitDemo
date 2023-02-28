import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
Products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in Products:
    prodcutName = product.find_element(By.XPATH, "div/h4").text
    if prodcutName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
alert = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
print(alert)