from selenium import webdriver

class Singleton(object):

    instance = None

    def __new__(cls, base_url, browser='chrome'):

        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            cls.base_url = base_url
            cls.browser = browser

            if browser == "chrome":
                # Create a new instance of the Chrome driver
                cls.driver = webdriver.Chrome()
            elif browser == "firefox":
                # Create a new instance of the Firefox driver
                cls.driver = webdriver.Firefox()
            else:
                print("Unsupported driver!")
        else:
            i = cls.instance
        return i