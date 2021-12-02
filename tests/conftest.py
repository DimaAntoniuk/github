import pytest
from selenium import webdriver

from src.driver.singleton import Singleton

@pytest.fixture(scope="session")
def browser():
    driver = Singleton()
    yield driver
    driver.driver.quit()