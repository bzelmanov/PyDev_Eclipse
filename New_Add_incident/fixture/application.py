from model.group import myIncident2
__init__ = 'bok'

from selenium import webdriver
import time

class myApplication:
    
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\tests\\JARs\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        
        
    def login(self, myGroup):
        driver = self.driver
        driver.get(myGroup.myUrl)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(myGroup.myEmail)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(myGroup.myPassword)
        driver.find_element_by_id("loginButton").click()


    def cancelIncident(self, myIncident):
        driver = self.driver
        driver.find_element_by_css_selector("div.icon.add_incident").click()
        driver.find_element_by_id("notes").clear()
        driver.find_element_by_id("notes").send_keys(myIncident.note1)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(myIncident.note2)
        driver.find_element_by_id("cancelNewIncident").click()


    def logout(self):
        driver = self.driver
        driver.find_element_by_css_selector("div.icon.home").click()
        driver.find_element_by_css_selector("div.down_arrow").click()
        driver.find_element_by_xpath("//li[@onclick=\"javascript:location.href='/logout/';\"]").click()
        
        
    def test_add_incident2(self, myIncident2):
        driver = self.driver
        driver.find_element_by_css_selector("div.icon.add_incident").click()
        driver.find_element_by_id("notes").clear()
        driver.find_element_by_id("notes").send_keys(myIncident2.note1)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(myIncident2.note1)
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_id("incident_tags_2211").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick='sendSelectedItems(); return false;']").click()
        time.sleep(2)
        driver.find_element_by_id("cancelNewIncident").click()
            
        
    def destroy(self):
        self.driver.quit()
            
        