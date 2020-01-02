from base.selenium_web_driver import seleniumDriver
from utilities import custom_logger as cl
import logging


class trustId210012Retrieval(seleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    _start_retrieval = '//*[@id="nav"]/input'
    _activation_code = 'var1'
    _account_password = 'var2'

    def start_retrieval(self):
        self.click_element(self._start_retrieval, locatorType='xpath')
    
    def activation_code(self):
        self.find_element(self._activation_code)
        self.paste_activation_code()

    def account_password(self, password):
        self.send_keys(password, self._account_password)

    def finish_retrieval(self):
        self.click_element(self._start_retrieval, locatorType='xpath')

    def retrieve_one_yr_validity_option(self, password):
        self.start_retrieval()
        self.activation_code()
        self.account_password(password)
        self.finish_retrieval()
