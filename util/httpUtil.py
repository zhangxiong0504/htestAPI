import requests
import json
from common.CommonData import CommonData
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type': 'application/json;charset=UTF-8'}
    def post(self,path,data):
        proxies=CommonData.proxies   #获取全局变量proxies
        host=CommonData.url          #获取全局变量url
        data_json=json.dumps(data)    #将data参数转为json格式
        if CommonData.token is not None:    #判断token是否为空，不为空则赋值
            self.headers['token']=CommonData.token
        resp_login = self.http.post(url=host+path,    #发起post请求
                         proxies=proxies,
                         data=data_json,
                         headers=self.headers
                                    )
        #assert resp_login.status_code == 200     #校验返回吗
        resp_dict=json.loads(resp_login.text)             #获取response响应的body值,将body值转为dict
        # resp_dict=json.loads(resp_json)       #将body值转为dict
        print(resp_login.text)

        return resp_dict                 #返回
    def  logout(self,path,data):
        proxies = CommonData.proxies  # 获取全局变量proxies
        host = CommonData.url  # 获取全局变量url
        data_json = json.dumps(data)  # 将data参数转为json格式
        if CommonData.token is not None:  # 判断token是否为空，不为空则赋值
            self.headers['token'] = CommonData.token
        resp_logout = self.http.post(url=host + path,  # 发起post请求
                                    proxies=proxies,
                                    data=data_json,
                                    headers=self.headers
                                    )

        # assert resp_logout.status_code == 200  # 校验返回吗
        resp_dict = json.loads(resp_logout.text)  # 获取response响应的body值,将body值转为dict
        # resp_dict=json.loads(resp_json)       #将body值转为dict

        return resp_dict  # 返




# proxies={'http':'http://localhost:0504'}   #代理
# headers={'Content-Type':'application/json;charset=UTF-8'}
# # headers['Content-Type']='application/json;charset=UTF-8'
# http=requests.session()
# resp=http.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    data='{"userName":"15735997914","password":"123456"}',
#                    headers=headers
#                    )
# # assert resp.status_code==200
# resp_dict=json.loads(resp.text)#json转python_dict
# token=resp_dict['object']['token']#获取token
# headers['token']=token #将token加到headers dict里
#
#
# data={'token':token}#创建了一个data的dict，添加了token数据
# data_json=json.dumps(data)#将python对象转成json
#
# resp=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                    proxies=proxies,
#                    data='{"token":"'+token+'"}',
#                    #data='data_json'
#                    headers=headers
#                    )
#
#
#
# print(resp.text)
# print(resp.headers)
# print(resp.status_code)
# print(resp.cookies)
# print(resp.history)

# class HttpUtil: