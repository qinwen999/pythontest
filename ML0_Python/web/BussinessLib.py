# -*- coding: utf-8 -*-

class Bussiness(object):
    driver = None

    def __init__(self, p_driver):
        self.driver = p_driver

    def login(self, user, pwd):
        self.driver.find_element_by_css_selector("button.btn.btn-login").click()
        self.driver.find_element_by_name("login_name").clear()
        self.driver.find_element_by_name("login_name").send_keys(user)
        self.driver.find_element_by_name("login_password").clear()
        self.driver.find_element_by_name("login_password").send_keys(pwd)
        self.driver.find_element_by_xpath("//button[@type='button']").click()