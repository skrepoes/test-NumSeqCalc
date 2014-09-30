# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UtInputempty(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ut_inputempty(self):
        driver = self.driver
        driver.get(self.base_url + "file:///C:/NumSeqCalc/wwwroot/index.html")
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("")
        driver.find_element_by_id("calcSubmit").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#calcError").text, r"^[\s\S]*Please enter a positive number\.[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
