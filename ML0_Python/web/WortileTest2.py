# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WortileTest2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://my.worktile.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wortile_test2(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("button.btn.btn-login").click()
        driver.find_element_by_name("login_name").clear()
        driver.find_element_by_name("login_name").send_keys("ml0tester")
        driver.find_element_by_name("login_password").clear()
        driver.find_element_by_name("login_password").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='button']").click()

        self.assertTrue(driver.find_element(By.CSS_SELECTOR,"i.wtfont.wtf-create"))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
