from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Singleton(object):

    instance = None

    def __new__(cls, browser='chrome'):

        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            cls.browser = browser

            if browser == 'chrome':
                # Create a new instance of the Chrome driver
                cls.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif browser == 'firefox':
                # Create a new instance of the Firefox driver
                cls.driver = webdriver.Firefox(GeckoDriverManager().install())
            else:
                print('Unsupported driver!')
        else:
            i = cls.instance
        return i