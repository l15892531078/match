# author：xintian   
# time:2020-06-17
#-*- coding: utf-8 -*-
import requests
import json
from config import HOST
import allure
class LoginClass:
    def api_login(self,inData,getSession = True):
        # 1- 路径-url
        login_url = f'{HOST}/authentification/gettoken'
        header = {'Content-Type': 'application/json'}
        payload = json.loads(inData)
        reps = requests.post(login_url, json=payload)
        reps.encoding = 'unicode_escape'  # 设置响应编码--显示中文
        if getSession:
            return reps.json()['resultMessage']['token']
        else:
            return reps.text







    # 1- 直接传
if __name__ == "__main__":
    print(LoginClass().api_login('{"application_id": "hypecore_sit", "secret": "Dtm28qR%k"}'))