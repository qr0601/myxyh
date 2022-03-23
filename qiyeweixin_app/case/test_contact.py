"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 22:28'
"""
import logging

import pytest
from selenium.common.exceptions import NoSuchElementException
from qiyeweixin_app.base.wework_app import WeWorkApp
import yaml
from faker import Faker

class TestContact:

    def setup_class(self):
        self.app = WeWorkApp()


    def setup(self):
        self.main = self.app.start().goto_main()
        logging.info('开始')
    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()
        logging.info('结束')


    # @pytest.mark.parametrize("name, phonenum",[["xiaohong", "15883625119"]])
    @pytest.mark.parametrize('name,phonenum', yaml.safe_load(open('../date/add.yaml'))['add_datas'])
    def test_addcontact(self,name, phonenum):
        logging.info("增加联系人")
        result = self.main.goto_addresslist(). \
            click_addmemeber().click_addbymenual().edit_member(name, phonenum).retrun_contactlist().check_member(name)
        assert  result

    # @pytest.mark.parametrize("name", ["xiaohong"])
    @pytest.mark.parametrize('name', yaml.safe_load(open('../date/add.yaml'))['delete_datas'])
    def test_deletecontact(self, name):
        logging.info("删除联系人")
        res = self.main.goto_addresslist().goto_member_information(name).goto_Information_details()
        try:

            res.delete_member()

        except NoSuchElementException:
            # logging.info("删除成功")
            print('删除成功')
