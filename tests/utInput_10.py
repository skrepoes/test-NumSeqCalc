# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UtInput10(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ut_input10(self):
        driver = self.driver
        driver.get(self.base_url + "file:///C:/NumSeqCalc/wwwroot/index.html")
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("10")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsSeq").text, r"^[\s\S]*1, 2, 3, 4, 5, 6, 7, 8, 9, 10[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1, 3, 5, 7, 9[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*2, 4, 6, 8, 10[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1, 2, C, 4, E, C, 7, 8, C, E[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1, 2, 3, 5, 8[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e)) 
    
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
