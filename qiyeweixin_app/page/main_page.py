"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 22:11'
"""
from appium.webdriver.common.mobileby import MobileBy
from qiyeweixin_app.base.wework_app import WeWorkApp
from qiyeweixin_app.page.addresslist_page import AddressListPage


class MainPage(WeWorkApp):
    _addresslist_element = (MobileBy.XPATH,
                            "//*[@text='通讯录']")

    def goto_addresslist(self):
        # click 通讯录
        self.find_click(*self._addresslist_element)
        return AddressListPage(self.driver)
