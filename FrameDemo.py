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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
time.sleep(3)
action.scroll_by_amount(1000, 1000)
driver.switch_to.frame("courses-iframe")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Courses").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.ID, "mousehover").click()
print("MY Git Code")
print("MY Git Stuff")

