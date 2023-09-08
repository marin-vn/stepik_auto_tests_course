from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
# говорим Selenium проверять в течение 12 секунд, пока цена дома не уменьшится до $100
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
)
button.click()
x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
button = browser.find_element(By.ID, "solve")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
