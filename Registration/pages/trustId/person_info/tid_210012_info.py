from base.selenium_web_driver import seleniumDriver
from selenium.webdriver.common.keys import Keys
from utilities import custom_logger as cl
import logging

class TrustId210012Info(seleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    _first_name = 'first_name'
    _last_name = 'last_name'
    _home_phone = 'hphone'
    _email = 'email'
    _mailing_state = '//*[@id="mailing_state"]/optgroup[6]/option[48]'
    _ind_country = '//*[@id="ind_country"]/option[210]'
    _password = 'password'
    _password_confirm = 'password_confirm'
    _question_1 = 'security_q1'
    _question_2 = 'security_q2'
    _question_3 = 'security_q3'
    _answer_1 = 'answer_1'
    _answer_2 = 'answer_2'
    _answer_3 = 'answer_3'
    _info_next = 'personal_info_confirm'
    _confirm_info = '/html/body/div[11]/div[3]/div/button[1]/span'

    def first_name(self, fname):
        self.send_keys(fname, self._first_name)

    def last_name(self, lname):
        self.send_keys(lname, self._last_name)
        self.send_keys(Keys.CONTROL, 'a')
        self.send_keys(Keys.CONTROL, 'c')

    def home_phone(self, hphone):
        self.send_keys(hphone, self._home_phone)

    def email_address(self, email):
        self.send_keys(email, self._email)

    def mailing_state(self):
        self.click_element(self._mailing_state, locatorType='xpath')

    def individual_country(self):
        self.click_element(self._ind_country, locatorType='xpath')

    def password_one(self, password):
        self.send_keys(password, self._password)

    def password_confirm(self, password):
        self.send_keys(password, self._password_confirm)

    def question_one(self, question):
        self.send_keys(question, self._question_1)

    def question_two(self, question):
        self.send_keys(question, self._question_2)

    def question_three(self, question):
        self.send_keys(question, self._question_3)

    def answer_one(self, answer):
        self.send_keys(answer, self._answer_1)

    def answer_two(self, answer):
        self.send_keys(answer, self._answer_2)

    def answer_three(self, answer):
        self.send_keys(answer, self._answer_3)

    def info_next(self):
        self.click_element(self._info_next)

    def confirm_info(self):
        self.click_element(self._confirm_info, locatorType='xpath')

    def info_one_yr_validity_option(self, fname, n, hphone, email, password, question, answer):
        self.first_name(fname)
        self.last_name(n)
        self.home_phone(hphone)
        self.email_address(email)
        self.mailing_state()
        self.individual_country()
        self.password_one(password)
        self.password_confirm(password)
        self.question_one(question)
        self.question_two(question)
        self.question_three(question)
        self.answer_one(answer)
        self.answer_two(answer)
        self.answer_three(answer)
        self.info_next()
        self.confirm_info()