"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 22:11'
"""
from appium.webdriver.common.mobileby import MobileBy
from qiyeweixin_app.base.wework_app import WeWorkApp


class AddMemberPage(WeWorkApp):

    def click_addbymenual(self):
        """
        click 手动输入添加
        :return:
        """
        self.find_click(MobileBy.XPATH,
                        "//*[@text='手动输入添加']")
        from qiyeweixin_app.page.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def retrun_contactlist(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/h86").click()
        from qiyeweixin_app.page.addresslist_page import AddressListPage
        return AddressListPage(self.driver)
    # def get_result(self):
    #     # get toast text
    #     element_toast = self.find(MobileBy.XPATH,
    #                               "//*[@class='android.widget.Toast']")
    #     result = element_toast.get_attribute("text")
    #     return result
