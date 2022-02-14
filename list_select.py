from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
link_1 = " http://suninjuly.github.io/selects2.html"
def summa(a,b):
    return a+b
try:
    browser = webdriver.Chrome()
    browser.get(link_1)
    find_a = browser.find_element(By.ID,"num1")
    a = int(find_a.text)
    find_b = browser.find_element(By.ID,"num2")
    b = int(find_b.text)
    s = str(summa(a,b))
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(s)
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()