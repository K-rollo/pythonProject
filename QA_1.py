from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("http://skleptest.pl/")

elem = driver.find_element(By.CSS_SELECTOR, "a[title='Contact']")
elem.click()
assert "Contact – Generic Shop" in driver.title

time.sleep(1)
driver.quit()
