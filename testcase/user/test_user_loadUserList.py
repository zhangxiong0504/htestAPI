import pytest
import requests
from common.CommonData import CommonData
from util.httpUtil import HttpUtil

class Test_loadUserList():
    http = HttpUtil()
    @pytest.mark.a
    def test_loaduserlist(self):
        path='/user/loadUserList'
        data={
                  "pageCurrent": 1,
                  "pageSize": 10,
                  "nickName": "",
                  "userName": "",
                  "regionId": 1
              }
        resp=self.http.post(path,data)
        assert resp['code']==200
        assert resp['object']['list'][1]['id']==CommonData.userId1

# if __name__ == '__main__':
#     pytest.main()