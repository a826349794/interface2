# 自媒体登录接口封装
import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiMp:
    # 初始化方法
    def __init__(self):
        # 登录url
        self.url_login = api.HOST+"/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url{}:".format(self.url_login))
    # 发布文章url
        self.url_article = api.HOST+"/mp/v1_0/articles"
        log.info("正在初始化自媒体发布文章url{}:".format(self.url_article))

    # 登录接口封装
    def api_login(self,mobile,code):
        # 请求数据
        data = {"mobile":mobile,"code":code}
        log.info("正在调用自媒体登录方法,测试数据:{}, 请求头为:api.headers{}".format(data,api.headers))
        # 调用post方法  此处用json
        return  requests.post(url=self.url_login,json=data,headers = api.headers)


    # 发布文章接口封装
    def api_mp_article(self,title,content):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channle_id: 7为数据库
        :cover :封面  0位自动选择
        :return:
        """
        # 请求数据
        data = {"title": title, "content": content, "channel_id": api.channel_id, "cover": {"type": 0, "images": []}}
        # 调用post方法
        log.info("正在调用自媒体发布文章方法,测试数据:{}, 请求头为:api.headers{}".format(data,api.headers))
        return requests.post(url=self.url_article, json=data, headers=api.headers)
