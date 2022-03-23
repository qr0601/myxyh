"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/6 21:37'
"""
from qiyeweixin_app.base.base_page import BasePage
from appium import webdriver

class WeWorkApp(BasePage):
    def start(self):
        if self.driver == None:
            print("driver == None")
            # 启动
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            # mac/linux:  adb logcat ActivityManager:I | grep "cmp"
            # windows:   adb logcat ActivityManager:I | findstr "cmp"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # 在启动的时候 ，不会清理缓存信息
            caps["noReset"] = True
            # 与远程服务建立连接，返回一个 session 对象
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("driver != None")
            # 热启动，launch 没有杀应用的操作，只是启动
            self.driver.launch_app()
            # 启动 给定的activity
            # self.driver.start_activity(packagename, activityname)
        return self

    def restart(self):
        # 重启
        pass

    def stop(self):
        # 停止
        self.driver.quit()

    def goto_main(self):
        # 入口
        from qiyeweixin_app.page.main_page import MainPage
        return MainPage(self.driver)
