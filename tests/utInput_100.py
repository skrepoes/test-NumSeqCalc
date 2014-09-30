# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UtInput100(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ut_input100(self):
        driver = self.driver
        driver.get(self.base_url + "file:///C:/NumSeqCalc/wwwroot/index.html")
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("100")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsSeq").text, r"^[\s\S]*1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1, 2, C, 4, E, C, 7, 8, C, E, 11, C, 13, 14, Z, 16, 17, C, 19, E, C, 22, 23, C, E, 26, C, 28, 29, Z, 31, 32, C, 34, E, C, 37, 38, C, E, 41, C, 43, 44, Z, 46, 47, C, 49, E, C, 52, 53, C, E, 56, C, 58, 59, Z, 61, 62, C, 64, E, C, 67, 68, C, E, 71, C, 73, 74, Z, 76, 77, C, 79, E, C, 82, 83, C, E, 86, C, 88, 89, Z, 91, 92, C, 94, E, C, 97, 98, C, E[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89[\s\S]*$")
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
