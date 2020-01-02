from base.selenium_web_driver import seleniumDriver
from utilities import custom_logger as cl
import logging

class TrustId210012Payment(seleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    _select_cc = 'ccPaymentType'
    _cc_number = 'creditCardNum'
    _security_code = 'card_security_code'
    _exp_month = '//*[@id="cc_exp_mm"]/option[7]'
    _exp_year = '//*[@id="cc_exp_yyyy"]/option[7]'
    _billing_address = 'billing_address1'
    _billing_city = 'billing_city'
    _billing_zip = 'billing_postal_code'
    _subscriber_agreement = 'Subscriber Agreement' # link text
    _subscriber_box = 'agree_checkbox'
    _submit_app = '//*[@id="next"]'


    def cc_button(self):
        self.clickElement(self._select_cc)

    def cc_payment(self, ccNumber):
        self.sendKeys(ccNumber, self._cc_number)

    def security_code(self, ccCode):
        self.sendKeys(ccCode, self._security_code)

    def exp_month(self):
        self.clickElement(self._exp_month, locatorType='xpath')
    
    def exp_year(self):
        self.clickElement(self._exp_year, locatorType='xpath')

    def billing_address(self, billAddress):
        self.sendKeys(billAddress, self._billing_address)
    
    def billing_city(self, billCity):
        self.sendKeys(billCity, self._billing_city)

    def billing_zip(self, billZip):
        self.sendKeys(billZip, self._billing_zip)

    def subscriber_agreement(self):
        self.clickElement(self._subscriber_agreement, locatorType='link')

    def subscriber_box(self):
        self.clickElement(self._subscriber_box)

    def submit_billing_info(self):
        self.clickElement(self._submit_app, locatorType='xpath')

    def payment_one_yr_validity_option(self, ccNumber, ccCode, billAddress, billCity, billZip):
        self.cc_button()
        self.cc_payment(cc_number)
        self.security_code(cc_code)
        self.exp_month()
        self.exp_year()
        self.billing_address(bill_address)
        self.billing_city(bill_city)
        self.billingZip(bill_zip)
        self.subscriber_agreement()
    
    def submit_application(self):
        self.subscriber_box()
        self.submit_billing_info()
