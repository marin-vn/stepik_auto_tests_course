from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
firstname = browser.find_element(By.NAME, "firstname")
firstname.send_keys("Vitaly")
lastname = browser.find_element(By.NAME, "lastname")
lastname.send_keys("Marin")
email = browser.find_element(By.NAME, "email")
email.send_keys("90marinvitalii@gmail.com")

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')

# загружаем файл
element = browser.find_element(By.NAME, "file")
element.send_keys(file_path)

# отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
