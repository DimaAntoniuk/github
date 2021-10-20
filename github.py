import time
from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = 'http://google.com'
STRING = 'github'

def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def go_to_url(driver, url):
    driver.get(url)

def find_page(driver, serach_string):
    searcher = driver.find_element_by_css_selector("input[type='text']")
    searcher.send_keys(f'{serach_string}')
    searcher.submit()

def check_result(driver, search_string):
    result = f'/search?q={search_string}' in driver.current_url
    return result

if __name__ == "__main__":
    my_driver = setup()
    go_to_url(my_driver, URL)
    find_page(my_driver, STRING)
    if check_result(my_driver, STRING):
        print('HOORAY!')
    else:
        print('WRONG URL(((')
    time.sleep(3)
    my_driver.quit()
