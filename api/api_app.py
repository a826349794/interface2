# app登录接口封装
import time
import requests
import api


class ApiApp:
    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.HOST+"/app/v1_0/authorizations"
        # 获取文章url
        self.url_article = api.HOST +"/app/v1_1/articles"

    # 登录封装
    def app_login(self,mobile,code):
        # 请求参数
        data = {"mobile": mobile, "code": code}
        # 调用post方法
        return  requests.post(url=self.url_login,json=data,headers = api.headers)

    # 获取文章接口封装
    def app_article(self):
        # 请求参数
        data = {"channel_id":api.channel_id ,"timestamp":int(time.time()),"with_top":0 }  #1包含置顶  0不包含置顶
        # 调用get方法
        return  requests.get(url=self.url_article,params=data,headers=api.headers)

