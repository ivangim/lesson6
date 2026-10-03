#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


#def test_dynamic_loading():
    #driver = webdriver.Chrome()

    #driver.get ("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    #wait = WebDriverWait(driver, 20)  
  
# Нажатие на кнопку "Start"  
    #click_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    #click_button.click()  
  
# Ожидание появления текста "Hello World"  
    #element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))  
    #assert element.text == ("Hello World!")  
  
# Создание скриншота страницы  
    #screenshot_path = 'screenshot.png'  
    #driver.save_screenshot(screenshot_path)

    #driver.quit()