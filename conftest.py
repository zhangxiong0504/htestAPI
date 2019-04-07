import pytest
import requests
import json
from util.httpUtil import HttpUtil
# http=HttpUtil()
from common.CommonData import CommonData


#session,module,class,function
# http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture1():
#     path="/sys/login"
#     data={'userName':CommonData.userName,'password':CommonData.passwword}
#     resp_login=http.post(path,data)
#
#     CommonData.token=resp_login['object']['token']
#     CommonData.userId =resp_login['object']['userId']
    print("登录成功")
#     yield
#     # logout_path="/sys/logout"
#     # logout_data={'token':CommonData.token}
#     # http.logout(logout_path,logout_data)
#     print("退出登录")


    # proxies = {'http': 'http://localhost:0504'}  # 代理
    # headers = {'Content-Type': 'application/json;charset=UTF-8'}
    # resp_login = http.post(url="http://192.168.1.203:8083/sys/login",
    #                  proxies=proxies,
    #                  data='{"userName":"15735997914","password":"123456"}',
    #                  headers=headers
    #                  )
    # assert resp_login.status_code == 200
    # resp_dict = json.loads(resp_login.text)  # json转python_dict
    # token = resp_login['object']['token']  # 获取token
    # print("登录成功")
    # yield
    # headers['token'] = token  # 将token加到headers dict里
    # resp_logout =http.post(url="http://192.168.1.203:8083/sys/logout",
    #                  proxies=proxies,
    #                  data=None,
    #                  headers=headers
    #                  )
    # assert resp_logout.status_code == 200
    # print("退出登录")