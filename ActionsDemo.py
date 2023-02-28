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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
#action.double_click()
#action.context_click() #RightClick
#action.drag_and_drop()
action.scroll_by_amount(1000,1000).perform()
time.sleep(3)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(3)
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
print("HI")
print("HI")
print("HI")
print("HI")
