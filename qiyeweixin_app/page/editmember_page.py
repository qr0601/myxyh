"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 22:12'
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from qiyeweixin_app.base.wework_app import WeWorkApp


class EditMemberPage(WeWorkApp):
    def edit_member(self, name, phonenum):
        from qiyeweixin_app.page.addmember_page import AddMemberPage

        self.find_send_keys(MobileBy.XPATH,
                            '//*[contains(@text, "姓名")]/../*[@text="必填"]',name)
        self.find_send_keys(MobileBy.XPATH,
                            "//*[contains(@text, '手机')]/..//*[@text='必填']",phonenum)

        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        return AddMemberPage(self.driver)

    def delete_member(self):
        logging.info("点击删除成员按键，弹出删除提示框")
        # self.find_click(MobileBy.XPATH, "//*[@text='删除成员']")
        self.swipe_find('删除成员').click()
        logging.info("点击确定，跳转到列表页面")
        self.find_click(MobileBy.XPATH, "//*[@text='确定']")
        from qiyeweixin_app.page.addresslist_page import AddressListPage
        return AddressListPage(self.driver)
