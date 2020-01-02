from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import custom_logger as cl
from traceback import print_stack
from selenium import webdriver
import logging
import time
from datetime import datetime
from time import localtime, strftime
import os

class SeleniumDriver():

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            self.log.info('Element: ' + locatorType + ' not supported ')
            return False

    def find_element(self, locator, locatorType='id'):
        element= None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Found Element by locatorType: ' + locatorType + 'and locator: ' + locator)
        except:
            self.log.info('Element not found by locatorType: ' + locatorType + 'and locator: ' + locator)
        return element

    def click_element(self, locator, locatorType='id'):
        try:
            element = self.findElement(locator, locatorType)
            element.click()
            self.log.info('Found Element by locatorType: ' + locatorType + 'and locator: ' + locator)
        except:
            self.log.info('Element not found by locatorType: ' + locatorType + 'and locator: ' + locator)
            print_stack()

    def send_keys(self, data, locator, locatorType='id'):
        try:
            element = self.findElement(locator, locatorType)
            element.send_keys(data)
            self.log.info('Found Element by locatorType: ' + locatorType + 'and locator: ' + locator)
        except:
            self.log.info('Element not found by locatorType: ' + locatorType + 'and locator: ' + locator)
            print_stack()

    def time_stamp(self):
        n = None
        n = self.driver.datetime.now().strftime('%a.%H.%M.%S.%f')
        return n

    def copy_activation_code(self):
        activationCode = None
        activationCode = self.driver.find_element_by_id('cert_id').text 
        return activationCode

    def paste_activation_code(self):
        activationCode = None
        activationCode = self.driver.copyActivationCode.send_keys(activationCode)
        return activationCode

    def element_present(self, locator, locatorType='id'):
        try:
            element = self.findElement(locator, locatorType)
            if element is not None:
                self.log.info('Element found by locatorType: ' + locatorType + 'and locator: ' + locator)
                return True
            else:
                self.log.info('Element not found by locatorType: ' + locatorType + 'and locator: ' + locator)
                return False
        except:
            self.log.info('Element not found by locatorType: ' + locatorType + 'and locator: ' + locator)

    def wait_for_element(self, locator, locatorType='id', timeout=10, pollFrequency=.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info('Element appeared ::' + str(timeout) + 
            ':: seconds before it was clickable')
            wait = WebDriverWait(self.b, 10, poll_frequency=.5,
                                    ignored_exceptions=[ElementNotSelectableException,
                                                        ElementNotVisibleException,
                                                        NoSuchElementException])
            element = wait.until(EC.element_to_be_clickable((byType, 'Stop Feature Stops 0')))
            self.log.info('Element appeared on site')
        except:
            self.log.info('Element didn\'t appear on site')
            print_stack()
        return element