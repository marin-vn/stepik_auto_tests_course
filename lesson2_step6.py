from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
checkbox = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()
radio = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
