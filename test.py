# -*- coding: UTF-8 -*-
from selenium import webdriver
from nose.tools import ok_, eq_
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    nowhandle = driver.current_window_handle
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(u"百度云管家")
    driver.find_element_by_id("su").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"百度云管家最新官方版下载_百度软件中心").click()
    time.sleep(2)
    allhandles = driver.window_handles
    for handle in allhandles:
        if handle != nowhandle:
            print handle
            driver.switch_to_window(handle)
    time.sleep(1)
    driver.find_element_by_css_selector("a.normal_download").click()
