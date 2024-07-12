from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locatorType, locator):
        element = None
        try:
            ByType = self.getByType(locatorType)
            element = self.driver.find_element(ByType, locator)
            print("Element Found with locatorType >> " + locatorType + " and locator >> " + locator)
        except:
            print("Element Not Found with locatorType >> " + locatorType + " and locator >> " + locator)
        return element

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "id":
            return By.ID
        else:
            print("Unable to find the locatorType by >>" + locatorType)
        return False

    def elementClick(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            element.click()
            print("Able to click on element with locatorType >> " + locatorType + " and locator >> " + locator)

        except:
            print("Not able to click on element with locatorType >> " + locatorType + " and locator >> " + locator)

    def sendKeys(self, data, locatorType, locator ):
        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            print("Sent Data To Locator Type: " + locatorType + " and locator: " + locator)
        except:
            print("Cannot Sent Data To Locator Type: " + locatorType + " and locator: " + locator)

    def isElementPresent(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            if element is not None:
                return True
            else:
                return False
        except:
            return False

    def waitForElement(self, locatorType, locator,
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     TimeoutException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
        return element

    def selectFromDropdown (self, data, locatorType, locator, bywhat):
        try:
            element = self.getElement(locatorType, locator)
            sel = Select(element)

            self.bywhat = bywhat.lower()
            if bywhat == 'value':
                sel.select_by_value(data)
            elif bywhat == 'index':
                sel.select_by_index(data)
            elif bywhat == "text":
                sel.select_by_visible_text(data)
            else:
                print("Invalid ByWhat for Selecting the item from drop down")

        except:
            print("Not able to select item in country drop down")

    def clearText (self, locatorType, locator):
        element = self.getElement(locatorType, locator)
        element.clear()

    def getInnerHeight(self):
        innerHeight = self. driver.execute_script("return window.innerHeight;")
        return innerHeight

    def scrollDown(self, innerHeight):
        self.driver.execute_script("window.scrollBy(0, innerHeight);")

    def switchToIFrame(self, byWhat, value):
        byWhat = byWhat.lower()
        if byWhat == "name":
            self.driver.switch_to.frame(value)
        if byWhat == "id":
            self.driver.switch_to.frame(value)
        if byWhat == "index":
            self.driver.switch_to.frame(value)
        else:
            print("Not able to switch to frame based on >> " + byWhat + " and " + value)

    def switchTodefaultContent(self):
        self.driver.switch_to.default_content()

    def switchToIFrameByLoopingAllIFrames(self, locatorType, locator):
        IframeList = self.driver.find_elements(By.XPATH, "//iframe")

        for i in range(len(IframeList)):
            self.switchToIFrame("index", IframeList[i])
            result = self.isElementPresent(locatorType,locator)
            if result:
                print("I frame Index is >> " + str(i))
                break
            self.switchTodefaultContent()
        return result







