from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем и заполняем поля
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("ivan@ivanov.org")

    # Явно указал расположение файла, нашел элемент и передал ему параметр
    file_path = "C:\\script_selenium\\test_primer.txt"
    file1 = browser.find_element_by_id("file")
    file1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка