from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
num1 = browser.find_element(By.ID, "num1")
num2 = browser.find_element(By.ID, "num2")
sum = int(num1.text) + int(num2.text)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
