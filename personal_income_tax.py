# -*- coding: UTF-8 -*-
import time
from nose.tools import assert_equal
from nose.tools import with_setup
from nose.tools import ok_,eq_
from selenium import webdriver
from webUI import webUI
class personal_income_tax(object):
    driver = webdriver.Chrome()
    def login(self, username, password):
        '''
        个税登录第一步，进入报税页面
        | username | pas |
        '''
        self.driver.maximize_window()
        self.driver.get("https://17dz.com/")
        self.driver.find_element_by_css_selector("a.homePage-button").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(0.3)
        self.driver.find_element_by_id("login").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[@id='enterTax']/a").click()
        time.sleep(1)

    def Tax_ex(self,ex1,ex2,ex3,ex4,ex5):
        '''
           进入报税页面后传入的参数分别为login的返回值
           |预期结果1|预期结果2|预期结果3|预期结果4|预期结果5|
           '''
        x1 = self.driver.find_element_by_xpath(".//*[@id='sidebar']/div[1]").text
        x2 = self.driver.find_element_by_xpath("//li[@id='normalAccount']/a/span").text
        x3 = self.driver.find_element_by_xpath("//li[@id='smallAccount']/a/span").text
        x4 = self.driver.find_element_by_xpath("//div[@id='taxBatchReport']/a").text
        x5 = self.driver.find_element_by_xpath("//div[@id='taxRecord']/a").text
        i=0
        list=[x1,x2,x3,x4,x5]
        exlist=[ex1,ex2,ex3,ex4,ex5]
        while(i<5):
            #ok_(list[i]==exlist[i],u'期望的是'+exlist[i]+u'但是发现的是'+list[i])
            #assert list[i]==exlist[i],i
            eq_(list[i],exlist[i])
            i=i+1
    def teardown(self):
        self.driver.quit()
if __name__ == "__main__":
    test=personal_income_tax()
    x=test.login("15658890633","tang7758521")
    test.Tax_ex(u'报税',u'一般纳税',u'小规模纳税人',u'个税批量',u'税金档案')

