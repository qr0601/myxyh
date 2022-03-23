"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 22:11'
"""
import logging
from time import sleep
from qiyeweixin_app.base.wework_app import WeWorkApp
from qiyeweixin_app.page.addmember_page import AddMemberPage


class AddressListPage(WeWorkApp):

    def click_addmemeber(self):
        # click 添加成员
        # self.find_click(MobileBy.XPATH,
        #                 "//*[@text='添加成员']")
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_member_information(self, name):
        logging.info(f"在通讯录列表点击成员：{name},跳转到成员信息页面")
        self.swipe_find(name).click()
        from qiyeweixin_app.page.Information_page import InformationPage
        return InformationPage(self.driver)

    def check_delete(self, name):
        sleep(2)
        logging.info(f"删除{name}成员成功")
        return self.swipe_find(name)

    def check_member(self, name):
        self.swipe_upward_find(name)
        return True
