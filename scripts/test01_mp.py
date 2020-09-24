import pytest

import api
from api.api_mp import ApiMp
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.tools import Tools

log = GetLog.get_logger()
class TestMp:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = ApiMp()
        log.info("正在获取ApiMp对象:{}".format(self.mp))
    # 登录接口 测试方法
    @pytest.mark.parametrize("mobile,code",read_yaml("mp_login.yaml"))
    def test01_mp_login(self,mobile,code):
        # 调用登录接口
        r= self.mp.api_login(mobile,code)
        log.info("正在调用登录接口:{}".format(r))
        print('登录的状态码为:',r.status_code)
        print('登录的结果为:',r.json())
        try:
           # 提取token
            Tools.common_token(r)
            # 断言
            Tools.common_assert(r)
        except Exception as  e:
            # 1.日志
            log.error(e)
            # 2. 抛异常
            raise e



    # 发布文章 接口测试方法
    # @pytest.mark.parametrize("title,content,channel_id",read_yaml("mp_article.yaml"))
    def test02_mp_article(self,title=api.title,content=api.content):
        # 调用发布文章接口
        r = self.mp.api_mp_article(title,content)
        log.info("正在调用发布文章接口:{}".format(r))

        try:
            # 提取文章id
            print('发布文章结果为:',r.text)
            print('发布文章的状态码为:',r.status_code)
            api.article_id= r.json().get("data").get("id")
            log.info("正在提取文章id:{}".format(api.article_id))
            print("提取的id为:",api.article_id)
            # 断言
            Tools.common_assert(r)
        except Exception as e:
            # 1.日志
            log.error(e)
            # 2. 抛异常
            raise  e
