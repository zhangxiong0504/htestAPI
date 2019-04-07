import pytest
import requests
import json
from common.CommonData import CommonData
from util.httpUtil import HttpUtil

class Test_Login():
    http = HttpUtil()
    def test_login_success(self):
        data={
            'userName': CommonData.userName,
            'password': CommonData.passwword,
        }
        resp=self.http.post('/sys/login',data)
        CommonData.token = resp['object']['token']
        assert resp['code']==200
        assert resp['msg'] == '操作成功'
        # assert resp['object']['userId'] ==123
    # def test_login_failed(self):
    #     data={
    #         'userName':CommonData.userName,
    #         'password':'456123',
    #     }
    #     resp=self.http.post('/sys/login',data)
    #     # assert resp['code']==310
    #     # assert resp['msg'] == '用户不存在'
    #     assert resp['code'] == 410
    #     assert resp['msg'] == '用户名或密码错误'
    # def test_login_failed1(self):
    #     data={
    #         'userName':"15735518559",
    #         'password':CommonData.passwword,
    #     }
    #     resp=self.http.post('/sys/login',data)
    #     assert resp['code']==301
    #     assert resp['msg'] == '用户不存在'
    # def test_login_failed2(self):
    #     data={
    #         'userName':CommonData.userName,
    #         'password':'',
    #     }
    #     resp=self.http.post('/sys/login',data)
    #     # assert resp['code']==310
    #     # assert resp['msg'] == '用户不存在'
    #     assert resp['code'] == 410
    #     assert resp['msg'] == '用户名或密码错误'
    # def test_login_failed3(self):
    #     data={
    #         'userName':'',
    #         'password':CommonData.passwword,
    #     }
    #     resp=self.http.post('/sys/login',data)
    #     # assert resp['code']==310
    #     # assert resp['msg'] == '用户不存在'
    #     assert resp['code'] == 3010
    #     assert resp['msg'] == '此账户禁止登录'
# @pytest.fixture()
# def my_fixtures():
#     print("login start")
#     yield
#     print("login end")
# @pytest.mark.debug
# def test_first():
#     print("登录：第一个测试用例")
#     assert 1 != 2

# @pytest.mark.info
# @pytest.mark.usefixtures("my_fixtures")
# def test_second():
#     print("登录：第二个测试用例")
#     assert 1 == 1
#
# def test_thrid():
#     print("第三个测试用例")
#     assert 'a' in "b"
#
# def test_four():
#     print("登录：第四个测试用例")
#     b=[1,2,3]
#     assert 3 in b
#
# @pytest.mark.usefixtures("my_fixtures")
# def test_five():
#     print("登录：第五个测试用例")
#     assert True

# def test_six():
#     print("登录：第六个测试用例")
#     assert assValue(3,5)
#
# def assValue(a,b):
#     if a>b:
#         return True
#     else:
#         return False
# if __name__ == '__main__':
#     pytest.main('-s')
# if __name__ == '__main__':
#     pytest.main()