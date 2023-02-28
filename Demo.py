import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ActualList = []

service_obj = Service("D:/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
Items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(Items)
print(count)
for item in Items:
    ActualList.append(item.find_element(By.XPATH, "h4").text)
    item.find_element(By.XPATH, "div/button").click()

print(ActualList)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

Calculate = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for calc in Calculate:
    sum = sum + int(calc.text)
print(sum)
total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

Discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert total > Discount
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()


