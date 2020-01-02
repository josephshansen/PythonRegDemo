from selenium import webdriver
from pages.trustId.overview.tid_210012_overview import trustId210012Overview
from pages.trustId.person_info.tid_210012_info import trustId210012Info
from pages.trustId.payment.tid_210012_payment import trustId210012Payment
from pages.trustId.tsadmin.tid_210012_approval import trustId210012Approval
from pages.trustId.retrieval.tid_210012_retrieval import trustId210012Retrieval
from base.selenium_web_driver import seleniumDriver
import unittest
import time
from datetime import datetime
from time import localtime, strftime

class Trust_Id_210012_test(unittest.TestCase):

    def test_1yr_210012(self):
        baseURL = 'https://secure-stg.identrust.com/tsapp/apply.jsp?AT=102&CT=210012'
        driver = webdriver.Chrome(r'V:\\Change Control\\Working Ops Docs\\Software\\chromedriver.exe')
        driver.get(baseURL)
        driver.maximize_window()

        TIO = TrustId210012Overview(driver)
        TIO.overview_one_yr_validity_option()

        TII = TrustId210012Info(driver)
        TII.info_one_yr_validity_option('Joseph', 'foolilu', '888-888-9889', 'joseph.hansen@identrust.com', 'QAteam1!', 'W', 'J')

        TIP = TrustId210012Payment(driver)
        TIP.payment_one_yr_validity_option('4111111111111111', '4561', '5225 Wiley Post Way', 'Salt Lake City', '84116')
        driver.switch_to.window(b.window_handles[0])
        TIP.submitApp()

        driver.get('https://secure-stg.identrust.com/tsadminapp/menu.jsp')
        TIA = TrustId210012Approval(b)
        TIA.approve_oneyr_validity_option(datetime.now().strftime('foolilu'))
        driver.switch_to.window(driver.window_handles[2])
        TIA.close_approve_window()
        driver.switch_to.window(driver.window_handles[0])
        TIA.getCode()
        driver.switch_to.window(driver.window_handles[2])
        TIA.close_code_window()
        driver.switch_to.window(driver.window_handles[0])
