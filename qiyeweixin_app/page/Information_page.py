"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:56'
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from qiyeweixin_app.base.wework_app import WeWorkApp

class InformationPage(WeWorkApp):
    __details = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]")

    def goto_Information_details(self):
        logging.info("点击更多按键，跳转到成员信息详情页面")
        self.find_click(*self.__details)
        return self.Information_details()


    def Information_details(self):
        logging.info("点击编辑成员按键，跳转到编辑成员页面")
        self.find_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        from qiyeweixin_app.page.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

