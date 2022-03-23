"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/9 21:51'
"""
import json
import mitmproxy.http
from mitmproxy import http

class Events:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and \
                "x=" in flow.request.url:
            # quote.json 是获取到的正常的响应体
            with open("quote.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    #状态码
                    200,
                    #响应体
                    f.read()
                )


    def response(self,flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and \
            "x=" in flow.request.url:
            data = json.loads(flow.response.text)
            #修改数据
            data["data"]["items"][0]["quote"]["name"] = "szr"
            new_data = self.recursion(data)
            #修改响应
            flow.response.text = json.dumps(new_data)

    # 递归
    def recursion(self,data):
        """
        :param data: 原始的数据
        :return: 在原始数据基础至上，修改float类型，对float类型做数据翻倍操作
        """
        if isinstance(data,dict):
            for k, v in data.items():
                data[k] = self.recursion(v)
        elif isinstance(data,list):
            data = [self.recursion(i) for i in data]
        elif isinstance(data, float):
            data = data * 2
        return data


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(["-p", "8080","-s", __file__])