import time
from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = 'http://google.com'

def find_page(driver, serach_string):
    searcher = driver.find_element_by_css_selector("input[type='text']")
    searcher.send_keys(f'{serach_string}')
    searcher.submit()

with webdriver.Chrome(ChromeDriverManager().install()) as driver:
    driver.get(URL)
    time.sleep(1)
    find_page(driver, 'github')
    time.sleep(3)