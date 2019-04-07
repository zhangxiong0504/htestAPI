import pytest
import requests
from common.CommonData import CommonData
from util.httpUtil import HttpUtil
import random
import allure

@pytest.mark.debug
@allure.feature("注册模块")
class Test_saveOrUpdateUser():
    http = HttpUtil()
    @allure.story("管理员登录")
    def test_login_success(self):
        data = {
            'userName': CommonData.userName,
            'password': CommonData.passwword,
        }
        resp = self.http.post('/sys/login', data)

        CommonData.token = resp['object']['token']
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'

    @allure.story("获取用户信息")
    def test_getuserinfo(self):
        path = '/sys/getUserInfo'
        data = {'token': CommonData.token}
        resp = self.http.post(path, data)
        assert resp['code'] == 200

    @allure.story("注册用户")
    def test_zhuce_saveorupdateuser(self):
        nickName = str(random.randint(10000000, 100000000))
        mobile= '135' + nickName
        path='/user/saveOrUpdateUser'
        data={'nickName':nickName,
              'userName':mobile,
              'telNo':'',
              'email':'',
              'address':'',
              'roleIds':'',
              'regionId':1,
              'regionLevel':1}
        resp=self.http.post(path,data)
        assert resp['code'] == 200
    #def test_saveorupdateuser(self):
        # nickName=str(random.randint(10000000, 10000000))
        # mobile='157'+nickName
        # data={
        #     "nickName": nickName,
        #     "userName": mobile,
        #     "telNo": "",
        #     "email": "",
        #     "address": "",
        #     "roleIds": "",
        #     "regionId": 1,
        #     "regionLevel": 1
        #    }
        # resp=self.http.post('/user/saveOrUpdateUser',data)
        # assert resp['code']==200

    #注册登录
    @allure.story("注册登录")
    def test_login(self):
        data = {
            'userName': CommonData.register_phone,
            'password': CommonData.registerpwd,
        }
        resp = self.http.post('/sys/login', data)
        CommonData.userId = resp['object']['userId']
        print(CommonData.userId)

        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'

    #查看用户列表
    @allure.story("显示管理员信息")
    def loaduserlist(self):
        data = {
                "pageCurrent": 1,
                "pageSize": 10,
                "nickName": "",
                "userName": "",
                "regionId": 1
                }
        resp = self.http.post('/user/loadUserList', data)
        # print(resp)
        assert resp['code'] == 200
        assert resp['object']['list'][1]['id'] == CommonData.userId
#
# if __name__ == '__main__':
#     pytest.main()