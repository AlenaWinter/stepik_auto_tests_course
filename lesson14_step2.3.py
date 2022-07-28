from selenium import webdriver
from selenium.webdriver.common.by import By


try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    import math
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
     
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла
    
