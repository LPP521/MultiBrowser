# -*- coding:UTF-8 -*-
import time
from selenium import webdriver
class webUI:
    def login(self,username,password):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://17dz.com/")
        driver.find_element_by_css_selector("a.homePage-button").click()
        time.sleep(0.5)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(0.3)
        driver.find_element_by_id("login").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li[4]/a").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//li[3]/a").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//li[4]/a").click()
        time.sleep(1)
        return driver

    def accounting(self,driver):
        driver.find_element_by_xpath("(//a[contains(@href, 'javascript:void(0)')])[5]").click()

if __name__ == "__main__":
    test=webUI()
    x=test.login("15658890633","tang7758521")
    test.accounting(x)