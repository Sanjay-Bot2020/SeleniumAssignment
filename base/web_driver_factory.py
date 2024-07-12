from selenium import webdriver

class Web_Driver_Factory():

    def __init__(self, whichBrowser):
        self.whichBrowser = whichBrowser

    def webDriverInstance(self):
        baseURL = "https://www.letskodeit.com/"

        if self.whichBrowser == "Firefox":
            driver = webdriver.Firefox()
        elif self.whichBrowser == "Chrome":
            driver = webdriver.Chrome()
        elif self.whichBrowser == "Edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver



