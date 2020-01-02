from base.selenium_web_driver import seleniumDriver
from selenium.webdriver.common.keys import Keys
from utilities import custom_logger as cl
import logging

class TrustId210012Overview(seleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _hid_smartcard = '//select[@id="storage"]/option[2]'
    _front_voucher = 'voucher_num'
    _validity_1yr = '//*[@id="sponsor_validity_opt"]/option[2]'
    _overview_nxt = "//div[@id='page_action']/input[@id='next']"

    def front_voucher(self, vou):
        self.sendKeys(vou, self._front_voucher, locatorType='id')

    def validity_period_one_yr(self):
        self.clickElement(self._validity_1yr, locatorType='xpath')

    def overview_next(self):
        self.clickElement(self._overview_nxt, locatorType='xpath')

    def overview_one_yr_validity_option(self):
        self.validityPeriod1Yr()
        self.overviewNext()
