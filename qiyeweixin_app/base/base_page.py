"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 21:36'
"""
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy

class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def refresh(self):
        self.driver.refresh()

    def find_click(self, by, locator):
        # 找到之后完成点击操作
        self.find(by, locator).click()

    def find_send_keys(self, by, locator, text):
        # 找到之后完成点击操作
        self.find(by, locator).send_keys(text)

    def back(self, num=3):
        # 封装返回方法
        for i in range(num):
            self.driver.back()

    def swipe_find(self, text, num=5):
        # num : 默认查找次数
        # 进入滑动查找，改变隐式等待时长，提高查找速度
        self.driver.implicitly_wait(1)

        # 滑动查找，通过外部传递的num次数，决定查找次数
        for i in range(0, num):
            try:
                element = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                # 滑动一页，继续查找
                size = self.driver.get_window_size()
                # self.driver.get_window_rect()
                width = size['width']
                height = size['height']
                # 'width', 'height'
                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 完成滑动操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")

    def swipe_upward_find(self, text, num=5):
        # num : 默认查找次数
        # 进入滑动查找，改变隐式等待时长，提高查找速度
        self.driver.implicitly_wait(1)

        # 滑动查找，通过外部传递的num次数，决定查找次数
        for i in range(0, num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                # 滑动一页，继续查找
                size = self.driver.get_window_size()
                # self.driver.get_window_rect()
                width = size['width']
                height = size['height']
                # 'width', 'height'
                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 完成滑动操作
                self.driver.swipe(start_x, end_y, end_x, start_y, duration)
            if i == num - 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")
