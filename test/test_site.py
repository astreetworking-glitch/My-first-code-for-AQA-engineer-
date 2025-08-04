from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
import time
import pytest



@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(30)
    yield browser
    browser.close()



def test_open_s6(browser):
    browser.get('https://demoblaze.com/')
    samsung = browser.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    samsung.click()
    title = browser.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/h2')



def test_two_Monitors(browser):
    browser.get('https://demoblaze.com/')
    monitor_link = browser.find_element(By.CSS_SELECTOR, 'a.list-group-item:nth-child(3)')
    monitor_link.click()
    time.sleep(5)
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 6