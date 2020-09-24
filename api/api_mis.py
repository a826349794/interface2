import requests

import api


class ApiMis:
    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.HOST + "/mis/v1_0/authorizations"
        # 查询文章url
        self.url_find = api.HOST +"/mis/v1_0/articles"
        # 审核文章url
        self.url_audit = api.HOST +"/mis/v1_0/articles"

    # 后台登录接口封装
    def mis_login(self,account,password):
        # 请求参数
        data ={"account":account,"password":password}
        # 调用post方法
        return requests.post(url=self.url_login,json=data,headers=api.headers )
    # 后台查询接口封装
    def mis_find(self):
        # 请求参数:title=test001&channel=html
        data = {'title':api.title,'channel':api.channel}
        # 调用get方法
        return requests.get(url=self.url_find,params=data,headers=api.headers)
    # 后台查询审核接口封装
    def mis_audit(self):
        # 请求参数
        data = {"article_ids":[api.article_id],"status":2}
        # 调用put方法
        return requests.put(url=self.url_audit,json=data,headers=api.headers)

