"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/22 23:26'
"""
import json
import logging
import requests


class BaseApi:
    # 对不同的请求协议进行封装
    def requests(self, requests: dict):
        if "url" in requests:
            return self.http_requests(requests)
        if "rpc" == requests.get("protocol"):
            return self.rpc_request(requests)

    def http_requests(self, data):
        r = requests.request(**data)
        logging.info(json.dumps(r.json(),indent=2,ensure_ascii=False))
        assert r.status_code == 200
        return r


    def rpc_request(self,data):
        pass

    def tcp_request(self):
        pass
