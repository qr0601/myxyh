"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/15 20:59'
"""


# 定义外函数
def demo(func):
    # 定义内函数
    def demo1():
        # 内函数调用传入函数
        func()
        return demo1

@demo
def szr():
    print("我是装饰器")
