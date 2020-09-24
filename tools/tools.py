import api

class Tools:
    # 提取token:
    @classmethod
    def common_token(cls,response):
        # 提取token
        token = response.json().get("data").get("token")
        # print("提取的token为:", token)
        # 追加到请求头中
        api.headers["Authorization"] = 'Bearer ' + token
        # print('追加后的headers为:', api.headers)
    # 断言
    @classmethod
    def common_assert(cls,response,status_code = 201):
        # 断言状态码
        assert status_code == response.status_code
        # 断言message
        assert "OK" == response.json().get("message")