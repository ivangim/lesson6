from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get ("https://gitflic.ru/")
    
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZjhlYTg1MWEtYzA5ZS00MDIzLWE4ZjktNmVhYzc1MjA0ZDUy",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "trye",
        "domain": "gitflic.ru"
    })
    
    driver.refresh()
    driver.get ("https://gitflic.ru/user/ivan_gim")
    
    url_user1 = driver.current_url
    print("https://gitflic.ru/user/ivan_gim:", {url_user1})
    
    driver.delete_all_cookies()
    driver.refresh()
    
    
    driver.add_cookie({
        "name": "SESSION",
        "value": "Njc1ODEzNTktMDM4My00MDBiLThhNzQtYTg2MDM1MWYwMjJm",
        "domain": "gitflic.ru"
    })
    
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "trye",
        "domain": "gitflic.ru"
    })
    
    driver.refresh()
    driver.get("https://gitflic.ru/user/tip88")
    
    url_user2 = driver.current_url
    print("https://gitflic.ru/user/tip88:", {url_user2})
    
    assert url_user1 != url_user2
    driver.quit()