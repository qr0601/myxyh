"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/21 22:32'
"""

from interface.api.base_api import BaseApi

class WeWork(BaseApi):
    token: str = None

    def get_token(self):
        date = {
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "method" : "get",
            "params" : {
                "corpid": "wwd48bdf0146365128",
                "corpsecret": "SjaAN0cGaeW2CJxAG-C5AnfbXAfTVQCJ2uDQ3fMvmkU"
            }
        }
        r=self.requests(date)
        self.token = r.json()['access_token']


