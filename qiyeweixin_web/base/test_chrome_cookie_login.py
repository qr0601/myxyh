"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/7 21:20'
"""
import time

import yaml
from selenium import webdriver

# 企业微信的cookie 有互踢机制。
class TestCookieLogin:
    def setup_class(self):
        self.drvier = webdriver.Chrome()

    def test_get_cookies(self):
        #访问企业微信主页/登录页面
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 等待20s，人工扫码操作
        time.sleep(20)
        # 等成功登陆之后，再去获取cookie信息
        cookie = self.drvier.get_cookies()
        # 将cookie存入一个文件
        # 打开文件的时候添加写入权限
        with open("../data/cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)

    def test_add_cookie(self):
        # 访问企业微信主页面
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 植入cookie
        for c in cookie:
            self.drvier.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def teardown(self):
        self.drvier.quit()
