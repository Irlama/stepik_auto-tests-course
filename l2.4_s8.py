# ждем нужный текст на странице
'''
1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver

# Открываем страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не будет <= 100$
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

# Скролим страницу вниз
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# Нажимаем кнопку book
browser.find_element_by_id("book").click()

# Находим чему равно значение x
x = browser.find_element_by_id("input_value").text
# Решаем математическую функцию - находим значение y
y = str(math.log(abs(12*math.sin(int(x))))) 

# Вводим значение y в поле ответа
browser.find_element_by_id("answer").send_keys(y) 
# Отправляем форму - нажимаем кнопку
browser.find_element_by_id("solve").click() 

