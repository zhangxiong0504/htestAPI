import pytest
import requests
from common.CommonData import CommonData
from util.httpUtil import HttpUtil

class Test_GetUserInfo():
    http = HttpUtil()
    def test_getuserinfo(self):
        path='/sys/getUserInfo'
        data={'token':CommonData.token}
        resp=self.http.post(path,data)
        assert resp['code']==200

# @pytest.fixture()
# def my_fixtures():
#     print("spec start")
#     # print("用户初始化操作")
#     yield
#     print("spec end")
#     # print("用户数据恢复")
# class Test():
#     @pytest.mark.debug
#     def test_first(this):
#         print("用户：第一个测试用例")
#         assert 1 != 2
#
#     @pytest.mark.debug
#     @pytest.mark.usefixtures("my_fixtures")
#     def test_second(this):
#         print("用户：第二个测试用例")
#         assert 1 == 1
#
#     def test_thrid(this):
#         print("用户：第三个测试用例")
#         assert 'a' in "b"
#
#     @pytest.mark.info
#     def test_four(this):
#         print("用户：第四个测试用例")
#         b=[1,2,3]
#         assert 3 in b
#
#     @pytest.mark.usefixtures("my_fixtures")
#     def test_five(this):
#         print("用户：第五个测试用例")
#         assert True

# def test_six():
#     print("用户：第六个测试用例")
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