from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID,"answer")
    find = browser.find_element(By.ID,"treasure")
    find = int(find.get_attribute("valuex"))
    x  = calc(find)
    input1.send_keys(x)
    ch_b = browser.find_element(By.ID,"robotCheckbox")
    ch_b.click()
    r_b = browser.find_element(By.ID,"robotsRule")
    r_b.click()
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    time.sleep(10)
    
finally:
    browser.quit()