"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:16'
"""
import logging
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from qiyeweixin_web.page.add_member_page import AddMemberPage
from qiyeweixin_web.base.base_page import BasePage
from qiyeweixin_web.page.contact_page import ContactPage
from qiyeweixin_web.page.wework_page import WeworkPage


class MainPageObject(WeworkPage):
    # _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 跳转通讯录页面的功能
    def goto_contact_page(self):
        return ContactPage()

    # 跳转添加成员页面的功能
    def goto_add_member_page(self):
        # 点击添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
