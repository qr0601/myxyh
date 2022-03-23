"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:19'
"""
import logging
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    封装一些和业务无关的重复代码
    是某些操作的底层
    """
    def __init__(self, base_driver=None):
        if base_driver is None:
            # 实例化
            self.driver = webdriver.Chrome()
            # 添加隐式等待的配置
            self.driver.implicitly_wait(3)

        else:
            self.driver:WebDriver = base_driver


    def find(self, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        """
        logging.info(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        if locator is None:
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by)
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator)
