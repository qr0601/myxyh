"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:18'
"""
import time

from selenium.webdriver.common.by import By

from qiyeweixin_web.base.base_page import BasePage
from qiyeweixin_web.page.wework_page import WeworkPage


class ContactPage(WeworkPage):
    # _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        pass

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")
        # 把元素列表 转换为名称列表，使用列表推导式（python-列表）
        member_list = [ele.text for ele in ele_list]
        # 成员的名称的列表
        return member_list
