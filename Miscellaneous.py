import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
#chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0, 200")
msg = driver.find_element(By.XPATH, "//table[@class='table-display']/tbody/tr[2]/td[2]").text
var = msg.split("with")[1].strip().split(" ")[0:6]

print(var)
time.sleep(3)
driver.find_element(By.ID, "name").send_keys(var)
time.sleep(2)
#driver.get_screenshot_as_file("Screen.png")