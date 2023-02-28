import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


browsersortedVeggies = []

service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElement:
    browsersortedVeggies.append(ele.text)

originalList = browsersortedVeggies.copy()

browsersortedVeggies.sort()

assert browsersortedVeggies == originalList