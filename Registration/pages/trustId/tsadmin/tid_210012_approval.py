from base.selenium_web_driver import seleniumDriver
from utilities import custom_logger as cl
from selenium.webdriver.common.keys import Keys
from pages.trustId.person_info.tid_210012_info import trustId210012Info
import logging

class trustId210012Approval(seleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    _account_mgmt = '//*[@id="acctCert"]/a'
    _lname_search = '//*[@id="mainContent"]/form/table/tbody/tr[4]/td[1]/input'
    _search = '//*[@id="mainContent"]/form/table/tbody/tr[8]/td[2]/input'
    _select_acct = '//*[@id="mainContent"]/form/p[3]/input'
    _approve_acct = '//*[@id="mainContent"]/form[1]/p/select/option[16]' 
    _update = '//*[@id="mainContent"]/form[1]/p/input'
    _popup_window = '//*[@id="popup"]/form/div/input'
    _activation_code = '//*[@id="mainContent"]/form[2]/p/select/optgroup[2]/option[6]'
    _continue = '//*[@id="mainContent"]/form[2]/p/input'
    _cert_id = 'cert_id'

    def account_mgmt(self):
        self.click_element(self._account_mgmt, locatorType='xpath')

    def lname_search(self, lname):
        self.send_keys(lname, self._lname_search, locatorType='xpath')

    def search_acct(self):
        self.click_element(self._search, locatorType='xpath')

    def select_acct(self):
        self.click_element(self._select_acct, locatorType='xpath')

    def approve_acct(self):
        self.click_element(self._approve_acct, locatorType='xpath')

    def update(self):
        self.click_element(self._update, locatorType='xpath')

    def approve_one_yr_validity_option(self, lname):
        self.account_mgmt()
        self.lname_search(lname)
        self.search_acct()
        self.select_acct()
        self.approve_acct()
        self.update()

##### Close Approve Account Window
    def close_approve_window(self):
        self.wait_for_element(self._popup_window, locatorType='xpath')
        self.click_element(self._popup_window, locatorType='xpath')

##### Get Activation Code
    def activation_code(self):
        self.click_element(self._activation_code, locatorType='xpath')

    def contine(self):
        self.click_element(self._continue, locatorType='xpath')

    def get_code(self):
        self.activation_code()
        self.contine()

##### Copy Code and close window
    def copyCode(self):
        self.wait_for_element(self._cert_id)
        self.copy_activation_code()

    def close_popup(self):
        self.click_element(self._popup_window, locatorType='xpath')
    
    def close_code_window(self):
        self.copy_code()
        self.close_popup()

    
