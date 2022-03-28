"""
__author__ = 'ceshiren_szr'
__time__ = '2022/3/21 22:19'
"""
from jsonpath import jsonpath

from interface.tag.tag import Tag


class Testwework:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()

    def test_search(self):
        r = self.tag.tag_search()
        assert r.json()['errcode'] == 0

    def test_add(self):
        data = [{"name": "tag_123"}, {"name": "tag_321"}]
        r = self.tag.tag_create(group_name="group_123", tag_list=data)
        assert r.json()['errcode'] == 0

        r = self.tag.tag_search()

        tag_name_list = jsonpath(r.json(), '$..tag[*].name')
        assert "tag_123" in tag_name_list and 'tag_321' in tag_name_list