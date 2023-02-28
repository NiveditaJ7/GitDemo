import re
import time
from idlelib.multicall import r

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
WindowOpen = driver.window_handles

driver.switch_to.window(WindowOpen[1])
time.sleep(5)
msg = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
var = msg.split("at")[1].strip().split(" ")[0]
print(var)

driver.switch_to.window(WindowOpen[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
