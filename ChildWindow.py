import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowOpen = driver.window_handles

driver.switch_to.window(WindowOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(WindowOpen[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
