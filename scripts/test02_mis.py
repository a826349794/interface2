from api.api_mis import ApiMis
from tools.tools import Tools


class TestMis:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.apimis = ApiMis()


    # 后台登录接口
    def  test01_mis_login(self,account="testid",password="testpwd123"):
        # 1.调用登录接口
        r = self.apimis.mis_login(account,password)

        # 提取token
        Tools.common_token(r)
        # 断言
        Tools.common_assert(r)



    # 后台查询接口
    def test02_mis_find(self):

        # 1.调用查询接口
        r= self.apimis.mis_find()

        # 2.断言
        # 200为int,不能加引号
        Tools.common_assert(r,status_code=200)

     # 后台查询审核接口
    def test03_mis_audit(self):

    # 1.调用审核接口
        r= self.apimis.mis_audit()


    # 2.断言
        Tools.common_assert(r)
