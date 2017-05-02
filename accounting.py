# -*- coding: UTF-8 -*-
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from nose.tools import assert_equal
from nose.tools import with_setup
from nose.tools import ok_,eq_
from selenium import webdriver
class accounting(object):
    driver = webdriver.Chrome()
    def login(self, username, password):
        '''
            登录第一步，进入记账页面
            | username | pas |
        '''
        self.driver.maximize_window()
        self.driver.get("https://17dz.com/")
        self.driver.find_element_by_css_selector("a.homePage-button").click()
        #time.sleep(2)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(0.3)
        self.driver.find_element_by_id("login").click()
        time.sleep(5)#此处为何不能使用 implicitly_wait()
        self.driver.find_element_by_xpath("//li[4]/a").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//li[3]/a").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//li[4]/a").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("inAccount").click()#进入亿企代账•记账界面
    def add_customer_init(self):
        '''
            添加客户信息 前提是在代税页面
        '''
        time.sleep(1)
        above = self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[2]/ul/li[8]")#悬浮在设置上
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(above).perform()  # 精髓 鼠标悬浮在上面的效果
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[2]/ul/li[8]/ul/li[2]").click()#进入辅助设置
        time.sleep(1)
        self.driver.find_element_by_xpath("//button").click()#添加新的客户
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//table[@id='clientList']/tbody/tr/td[2]").click()#点击新增
        time.sleep(0.5)
        self.driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(u"客户1")
    def add_supplier_init(self):
        '''
            添加供应商信息 前提是在代税页面
        '''
        time.sleep(1)
        above =self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[2]/ul/li[8]")  # 悬浮在设置上
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(above).perform()  # 精髓 鼠标悬浮在上面的效果
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[2]/ul/li[8]/ul/li[2]").click()  # 进入辅助设置
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div[2]").click()#进入供应商界面
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//button").click()  # 添加新的供应商
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@id='supplierList']/tbody/tr/td[2]").click()#选中第一烂
        time.sleep(1)
        self.driver.find_element_by_xpath("//td[2]/input").clear()
        self.driver.find_element_by_xpath("//td[2]/input").send_keys(u"供应商1")
    def set_subject(self):
        '''
            设置科目信息 前提是在代税页面
            启用了客户辅助，客户信息为【客户1】
            启用了供应商辅助，供应商信息为【供应商1】
            启用了存货辅助
            启用了数量核算，单位为【kg】
            启用了外币核算，外币代码为【USD】

        '''
        time.sleep(1.5)
        above = self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[2]/ul/li[8]")  # 悬浮在设置上
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(above).perform()  # 精髓 鼠标悬浮在上面的效果
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='mainContent']/div/div/div[2]/ul/li[8]/ul/li").click()#进入科目与期初
        time.sleep(2)
        # while(1):
        #     self.driver.find_element_by_xpath("//ins").click()
        #     cho1=self.driver.find_element_by_xpath("//ins").is_selected()
        #     print cho1
        #     if (cho1==True):
        #         print "ok"
        #         break
        #     else:
        #         print "wrong"
        #         time.sleep(1)
        self.driver.find_element_by_xpath("//ins").click()
        self.driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/div[2]/div/label[2]/div/ins").click()
        self.driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/div[2]/div/label[3]/div/ins").click()#显示上方的所有勾选框
        self.driver.find_element_by_xpath("//label[4]/div/ins").click()
        time.sleep(1)
        while(True):
            role=self.driver.find_element_by_xpath(".//*[@id='subjectList']/tbody/tr[6]/td[3]/div/button").get_attribute("title")
            if(role==u"客户"):
                break
            else:#如果角色不是客户的话 强制转换成将客户
                self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[6]/td[3]/div/div/ul/li[2]/a/span").click()
        time.sleep(1)
        while (True):
            role = self.driver.find_element_by_xpath(".//*[@id='subjectList']/tbody/tr[9]/td[3]/div/button").get_attribute("title")
            if (role == u"供应商"):
                break
            else:  # 如果角色不是供应商的话 强制转换成供应商
                self.driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[9]/td[3]/div/div/ul/li[3]/a/span").click()
        time.sleep(1)
        while (True):
            role = self.driver.find_element_by_xpath(".//*[@id='subjectList']/tbody/tr[22]/td[3]/div/button").get_attribute("title")
            if (role == u"存货"):
                break
            else:  # 如果角色不是存货的话 强制转换成存货
                self.driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[22]/td[3]/div/div/ul/li[4]/a/span").click()
        time.sleep(1)
        while (True):
            role = self.driver.find_element_by_xpath(".//*[@id='subjectList']/tbody/tr[20]/td[4]/input").get_attribute("value")
            if (role == "kg"):
                break
            else:  # 确保启用了数量核算，单位为【kg】
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[20]/td[4]/span").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[20]/td[4]/input").clear()
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[20]/td[4]/input").send_keys("kg")
        time.sleep(1)
        while (True):
            role = self.driver.find_element_by_xpath("//tr[25]/td[5]/input").get_attribute("value")
            if (role == "USD"):
                break
            else:  # 确保启用了外币核算，单位为【USD】
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[25]/td[5]/span").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//table[@id='subjectList']/tbody/tr[25]/td[5]/input").clear()
                self.driver.find_element_by_xpath("//tr[25]/td[5]/input").send_keys("USD")
        time.sleep(1)
    def test_add_abstract(self,name):
        '''
           添加摘要界面 结束后界面在路凭证页面
            |  name |
        '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()#进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").clear()
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(name)
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='accDocWrapper']/div[2]/div[2]/div/ul/li").click()#输完数据后点击进入别的数据狂，然后获取数据与预期对比
        real_msg = self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").get_attribute("value")
        eq_(real_msg,name)
    def test_add_accounting_subjects(self,name):
        '''
            添加内容为库存界面 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()#进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()#点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1001 库存现金").click()#选择库存现金、
        real_msg=self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[3]").get_attribute("title")#进入会计科目
        eq_(real_msg,name)
    def test_add_accounts_receivable(self,name):
        '''
            添加内容为应收赃款 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()#进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()#点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"112201 应收账款-内销帐款").click()
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"客户1").click()
        time.sleep(0.5)
        real_msg1 =self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[3]").get_attribute("title")  # 进入会计科目
        real_msg2=self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[4]").text  # 进入会计科目
        real_msg=real_msg1+real_msg2
        eq_(real_msg,u"应收账款-内销帐款-客户1")
    def test_add_advance_payment(self,name):
        '''
            添加内容预付账款 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()  # 点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1123 预付账款").click()
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"供应商1").click()
        time.sleep(0.5)
        real_msg1 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[3]").get_attribute("title")  # 进入会计科目
        real_msg2 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[4]").text  # 进入会计科目
        real_msg=real_msg1+real_msg2
        eq_(real_msg,name)
    def test_add_stock_goods(self,name):
        '''
            添加内容为库存商品 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()  # 点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"140501 库存商品-内销").click()
        time.sleep(0.1)
        self.driver.find_element_by_link_text("123").click()#存货类型名字
        time.sleep(0.5)
        real_msg1 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[3]").get_attribute("title")  # 进入会计科目
        real_msg2 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/p/span[4]").text  # 进入会计科目
        real_msg = real_msg1 + real_msg2
        eq_(real_msg, name)
    def test_add_raw_material(self,amount1,amount2):
        '''
            添加内容为原材料 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()  # 点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1403 原材料").click()
        time.sleep(0.1)
        self.driver.find_element_by_name("amount").clear()
        self.driver.find_element_by_name("amount").send_keys(amount1)#输入数量
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[3]/div/div[6]").click()#点击借方金额
        time.sleep(0.5)
        self.driver.find_element_by_name("cash").clear()
        self.driver.find_element_by_name("cash").send_keys(amount2)#输入借方金额
        self.driver.find_element_by_css_selector("div.app-docs-nav.acd-top-area").click()
        time.sleep(0.5)
        real_msg1=self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/div[2]/p/span[1]").text
        real_msg2=self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/div[2]/p/span[3]").text
        eq_(real_msg1,str(amount1))
        eq_(real_msg2,str(amount2/amount1))
    def test_add_difference(self,money,rate,balance):#默认情况下一定不能保存，否则会有余额累加
        '''
            添加内容为商品经销差价 结束后界面在路凭证页面
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()  # 点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1407 商品进销差价").click()
        time.sleep(0.1)
        self.driver.find_element_by_name("fcurCash").clear()
        self.driver.find_element_by_name("fcurCash").send_keys(money)
        self.driver.find_element_by_name("exchangeRate").clear()
        self.driver.find_element_by_name("exchangeRate").send_keys(rate)
        time.sleep(0.1)
        self.driver.find_element_by_css_selector("div.app-docs-nav.acd-top-area").click()
        real_msg1 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/div[3]/p/span[2]").text
        real_msg2 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/div[3]/p/span[3]").text
        real_msg3 = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[2]/div[1]/div[1]/span[1]").text
        money='%.2f'%money#保留两位小树
        total='%.2f'%balance#保留两位小树
        eq_(real_msg1, str(money))
        eq_(real_msg2, str(rate))
       # print real_msg3
        eq_(real_msg3, str(total))
    def test_del_date_low1(self):#提示元素不可见 隐藏元素
        '''
           删除第一行的内容
             |  name |
         '''
        self.test_add_abstract("test")
        time.sleep(0.2)
        print "添加摘要完成"
        real_msg = self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").get_attribute("value")
        print real_msg
        above = self.driver.find_element_by_xpath("//div[6]/i")  # 悬浮在设置上
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(above).perform() # 精髓 鼠标悬浮在上面的效果
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[6]/i").click()
        time.sleep(0.5)
        real_msg = self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").get_attribute("value")
        print real_msg+"123"
    def test_add_money_borrow(self,money):#只能输入n千
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[3]/div/div[6]").click()#输入借方金额
        self.driver.find_element_by_name("cash").clear()
        self.driver.find_element_by_name("cash").send_keys(money)
        self.driver.find_element_by_css_selector("div.app-docs-nav.acd-top-area").click()
        real_msg = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[3]/div/div[6]").text
        eq_(real_msg,str(money/1000))
    def test_add_money_loan(self,money):#只能输入n千
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        #self.driver.find_element_by_css_selector("div..firepath-matching-node").click()
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[4]/div/div[7]").click()#输入贷方金额
        self.driver.find_element_by_xpath("(//input[@name='cash'])[2]").clear()
        self.driver.find_element_by_xpath("(//input[@name='cash'])[2]").send_keys(money)
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//div[@id='accDocWrapper']/div[2]/div").click()
        real_msg = self.driver.find_element_by_xpath(".//*[@id='certifList']/div[1]/div[4]/div/div[6]").text
        eq_(real_msg, str(money / 1000))
    def test_check_date(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        period_of_genus=self.driver.find_element_by_xpath(".//*[@id='mainContent']/div/div[1]/div[1]/div[3]/input").get_attribute("value")#获取所属期
        billing_date=self.driver.find_element_by_xpath(".//*[@id='accDocWrapper']/div[2]/div[1]/span[1]/input[2]").get_attribute("value")#获取默认记账期
        if period_of_genus== "2016年08月":
            billing_date_should="2016-08-31"
        elif period_of_genus== "2016年09月":
            billing_date_should="2016-09-30"
        eq_(billing_date,billing_date_should)
    def test_document_preservation(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").clear()
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys("test")  # 输入第一行的摘要
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div[2]/div/p").click()  # 点击这个元素会出现下拉框
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1407 商品进销差价").click()
        time.sleep(0.1)
        self.driver.find_element_by_name("fcurCash").clear()
        self.driver.find_element_by_name("fcurCash").send_keys(2000)  # 输入的数字为2000
        time.sleep(0.1)
        self.driver.find_element_by_name("exchangeRate").clear()
        self.driver.find_element_by_name("exchangeRate").send_keys(6)
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div[2]/div/div").click()
        self.driver.find_element_by_xpath("//div[@id='certifList']/div[2]/div/textarea").clear()
        self.driver.find_element_by_xpath("//div[@id='certifList']/div[2]/div/textarea").send_keys(u"测试用")  # 在第二行输入摘要
        time.sleep(0.2)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div[2]/div[2]/div/p").click()
        time.sleep(0.1)
        self.driver.find_element_by_link_text(u"1101 短期投资").click()  # 在第二行选择会计科目
        time.sleep(0.2)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div[2]/div[4]/div/div[5]").click()
        self.driver.find_element_by_xpath("(//input[@name='cash'])[4]").clear()
        self.driver.find_element_by_xpath("(//input[@name='cash'])[4]").send_keys("12000")  # 输入贷方金额用来平账
    def test_document_preservation_success(self):
        self.test_document_preservation()
        time.sleep(0.5)
        self.driver.find_element_by_id("saveBtn").click()
        time.sleep(0.2)
        prompt=self.driver.find_element_by_xpath("html/body/div[9]").text
        eq_(prompt,u"保存成功")
    def test_document_preservation_fail(self):
        self.test_add_difference(2000,6)
        self.test_add_abstract("test")
        time.sleep(0.5)
        self.driver.find_element_by_id("saveBtn").click() #点击保存按钮
        time.sleep(0.2)
        prompt=self.driver.find_element_by_xpath("html/body/div[9]").text
        eq_(prompt,u"借贷不平衡")
    def test_print(self):
        self.test_document_preservation()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='accDocWrapper']/div/div[2]/button").click()#点击打印
        time.sleep(2)
        title=self.driver.title
        print title
    def test_save_template(self):
        self.test_document_preservation()
        time.sleep(0.5)
        self.driver.find_element_by_name("openTmplBtn").click()#点击保存
        time.sleep(1)
        title=self.driver.find_element_by_xpath(".//*[@id='createTmplModal']/div/div/div[1]/h4").text
        time.sleep(0.1)
        eq_(title,u"新增凭证模板")
    def test_save_template_success(self,name):
        '''
            保存模版成功的情况下
              |  name |
          '''
        self.test_save_template()
        self.driver.find_element_by_name("tmplName").clear()
        self.driver.find_element_by_name("tmplName").send_keys(name)
        time.sleep(0.1)
        self.driver.find_element_by_name("createTmplSave").click()#点击保存
        time.sleep(1)
        msg=self.driver.find_element_by_xpath("html/body/div[9]").text
        print msg
    def test_del_template(self):
        '''
           删除模板 默认删除第一个
             |  name |
         '''
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()#以下步骤是删除模板用的
        time.sleep(0.2)
        self.driver.find_element_by_link_text(u"使用模板").click()
        time.sleep(1.2)
        above = self.driver.find_element_by_xpath(".//*[@id='accDocTmplList']/tbody/tr[1]/td[2]/i[2]")  # 悬浮在设置上
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(above).perform()  # 精髓 鼠标悬浮在上面的效果
        time.sleep(0.5)
        self.driver.find_element_by_xpath(".//*[@id='accDocTmplList']/tbody/tr[1]/td[2]/i[2]").click()
        time.sleep(0.1)
        self.driver.find_element_by_name("ok").click()
    def test_shortcut_key_e(self):
        '''
            以下为快捷键ctrl+e的操作
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys("111111")#此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL,'e')
        time.sleep(0.5)
        msg=self.driver.find_element_by_xpath(".//*[@id='createTmplModal']/div/div/div[1]/h4").text
        time.sleep(0.5)
        eq_(msg,u"新增凭证模板")
    def test_shortcut_key_q(self):
        '''
            以下为快捷键ctrl+q的操作
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(
            "111111")  # 此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL, 'q')
        time.sleep(0.5)
        msg = self.driver.find_element_by_xpath(".//*[@id='accDocTmplBody']/div/div[1]/table/tbody/tr/td[2]").text
        time.sleep(0.1)
        eq_(msg, u"凭证模板名称")
    def test_shortcut_key_r(self):
        '''
            以下为快捷键ctrl+r的操作
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(
            "111111")  # 此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL, 'r')
        time.sleep(0.2)
        msg = self.driver.find_element_by_xpath("html/body/div[9]").text
        time.sleep(0.1)
        eq_(msg, u"没有录入有效的会计分录信息")
    def test_shortcut_key_updown(self):
        '''
            以下为快捷键ctrl+up的操作
             |  name |
         '''
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/ul/li[2]/i").click()  # 进入录凭证页面
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys("111111")  # 此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        msg1=int(self.driver.find_element_by_xpath(".//*[@id='accDocWrapper']/div[2]/div[1]/span[1]/input[1]").get_attribute("value"))
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL, Keys.UP)#翻到上一页,也是保存着的最后一夜
        time.sleep(0.2)
        msg2=int(self.driver.find_element_by_xpath(".//*[@id='accDocWrapper']/div[2]/div[1]/span[1]/input[1]").get_attribute("value"))
        eq_(msg1-msg2,1)
        self.driver.find_element_by_css_selector("div.app-edit-brief-area").click()
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(
            "111111")  # 此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL,Keys.UP)  # 翻到上一页,也是保存着的最后一夜
        time.sleep(0.2)
        self.driver.find_element_by_css_selector("div.app-edit-brief-area").click()
        time.sleep(0.1)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys("111111")  # 此处一定要随便输入些什么才能使下面的快捷键使用
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//div[@id='certifList']/div/div/textarea").send_keys(Keys.CONTROL,Keys.DOWN)  # 翻到上一页,也是保存着的最后一夜
        time.sleep(0.2)
        msg3 = int(self.driver.find_element_by_xpath(".//*[@id='accDocWrapper']/div[2]/div[1]/span[1]/input[1]").get_attribute("value"))
        eq_(msg3,msg2)

if __name__ == "__main__":
    test=accounting()
    test.login('15658890633','tang7758521')
    test.test_shortcut_key_updown()