"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:46'
"""
from qiyeweixin_web.page.main_page import MainPageObject


class TestAddMember:
    def setup_class(self):
        """
        用例执行前的准备工作： 对象的初始化
        在一条case 当中，尽量就使用同一个url。
        """
        self.main = MainPageObject()
        self.main.login()
    def teardown_class(self):
        """
        退出driver 进程
        :return:
        """
        self.main.driver.quit()


    def teardown(self):
        """
        保证每一条用例开始的时候，执行状态是正确。
        回复到用例的初始页面
        :return:
        """
        self.main.back_start_page()

    def test_add_member(self):
        # 1. 点击添加成员，跳转到添加成员页面
        # 2. add member 的操作
        # 3. 获取通讯录页面的成员列表（实际结果）
        name = "伊泽瑞尔4"
        mem_list = self.main. \
            goto_add_member_page(). \
            add_member(name, "010442", "18900112222"). \
            get_member_list()
        # 4 断言 实际结果也就是成员列表 是否符合预期
        assert name in mem_list

    def test_add_member_fail(self):
        """
        当手机号码格式输入错误，有没有错误提示
        :return:
        """
        name = "伊泽瑞尔5"
        res = self.main.goto_add_member_page().add_member_fail(name, "0101233", "009")
        assert "请填写正确的手机号码" in res
