import requests
import json
from common.CommonData import CommonData
from util.httpUtil import HttpUtil
import allure
import pytest

@allure.feature("修改密码模块")
class Test_ChangePwd():
    http = HttpUtil()
    @allure.story('修改密码成功')
    def test_changepwd_success(self):
        data={
            'token':CommonData.token,
            'userId':CommonData.userId,
            'userName':CommonData.userName,
            'oldPwd': CommonData.passwword,
            'password':CommonData.newpwd
        }
        resp=self.http.post('/sys/changePwd',data)
        assert resp['code']==200
        assert resp['msg'] == '操作成功'

# if __name__ == '__main__':
#     pytest.main()