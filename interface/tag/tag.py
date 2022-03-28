"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/22 23:35'
"""

from interface.api.wework_api import WeWork


class Tag(WeWork):
    # 企业微信的企业客户标签功能
    def tag_search(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "method": "get",
            "params": {
                "access_token": self.token,
            }
        }
        r = self.requests(data)

        return r

    def tag_create(self, group_name, tag_list, **kwargs):
        """

        :param group_name:
        :param tag_list:[{}]
        :return:
        """
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                "group_name": group_name,
                "tag": tag_list,
            }
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": "post",
            "params": {
                "access_token": self.token,
            },
            "json": json_data
        }
        return self.requests(data)

    def tag_delete(self, tag_id_list):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token,
            },
            "json": {
                "tag_id": tag_id_list
            }
        }
        return self.requests(data)

    def clear(self):
        r = self.tag_search()
        tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        r = self.tag_delete(tag_id_list)
        return r
