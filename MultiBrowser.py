# -*- coding:UTF-8 -*-
import time
import shutil
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
class MultiBrowser:
    def MB(self,address,browser_name):
        localtime = time.strftime('%Y-%m-%d-%H-%m', time.localtime(time.time()))  # 获取当前的时间
        chrome_options = Options()
        chrome_options.binary_location =address
        driver = webdriver.Chrome(chrome_options=chrome_options)  # chrome内核的浏览器 操作方法。类似chrome
        driver.maximize_window()
        driver.get('http://www.17dz.com')
        time.sleep(1)
        fname = localtime + browser_name + "-up.jpg"
        driver.get_screenshot_as_file(fname)
        shutil.move(fname, "pic")
        js = "var q=document.body.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(0.5)
        fname = localtime + browser_name + "-down.jpg"
        driver.get_screenshot_as_file(fname)
        shutil.move(fname, "pic")
        time.sleep(0.5)
        driver.quit()

if __name__ == "__main__":
    mb1=MultiBrowser();
    mb1.MB(r'F:\Program Files\360Chrome\Chrome\Application\360chrome.exe',"360")
