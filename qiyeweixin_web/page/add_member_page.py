"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:19'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from qiyeweixin_web.page.contact_page import ContactPage
from qiyeweixin_web.page.wework_page import WeworkPage


class AddMemberPage(WeworkPage):
    _INPUT_USERNAME = (By.ID, "username")


    def add_member(self, username, accid, phone):
        """
        添加成员功能
        ，添加成功后返回通讯录页面
        """
        # self.driver.find_element(By.ID, "username").send_keys("金克斯3")
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        sleep(10)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [ele.text for ele in eles]
        return error_list
