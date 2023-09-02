import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)
def test_check_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == "Сurrent weather and forecast - OpenWeatherMap"

def test_fill_searh_city_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('Boston')
    time.sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[class="button-round dark"]')
    search_button.click()
    driver.implicitly_wait(5)
    search_option = driver.find_element(By.CSS_SELECTOR, "div.search-block > div.search > div > ul > li:nth-child(1) > span:nth-child(1)")
    search_option.click()
    time.sleep(5)
    expected_city = 'Boston, US'
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.current-container.mobile-padding > div:nth-child(1) > h2')
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city

