# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddIncident(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\tests\\JARs\\chromedriver_win32\\chromedriver.exe")
        #self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #self.base_url = "https://docit-preprod.stopit.fm/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_incident(self):
        driver = self.driver
        driver.get("https://docit-preprod.stopit.fm/")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Stopit1234")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("tj2@stopit.fm")
        driver.find_element_by_id("loginButton").click()
        driver.find_element_by_css_selector("div.icon.add_incident").click()
        driver.find_element_by_id("notes").clear()
        driver.find_element_by_id("notes").send_keys("123")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("123")
        driver.find_element_by_id("cancelNewIncident").click()
        driver.find_element_by_css_selector("div.icon.home").click()
        driver.find_element_by_css_selector("div.down_arrow").click()
        driver.find_element_by_xpath("//li[@onclick=\"javascript:location.href='/logout/';\"]").click()
       
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
