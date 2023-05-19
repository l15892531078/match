from config import HOST
import requests
import json
from Lib.ApiLogin import LoginClass
from Lib.GetExcelData import getExcelData
class ProductClass:
    # 1- 列出推荐商品
    def list_product(self, token, inData):
        api_url = f'{HOST}/preForMinistore/getPersonalizedProductLlistPage'
        headers = {
            'Authorization' : f'Bearer {token}'
        }
        inData = json.loads(inData)
        reps = requests.post(api_url, headers=headers, json=inData)
        reps.encoding = 'unicode_escape'
        return reps.text

    #3- 删除课程
    def delete_all_lesson(self, session, inId):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = {'action': 'delete_course',
                   'id': int(inId)
                   }
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    def delete_lesson(self, session, inData):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = inData
        reps = requests.delete(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

    def modify_lesson(self, session, inData):
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = inData
        reps = requests.put(api_url, data=payload,cookies=user_cookie)
        reps.encoding = 'unicode_escape'
        return reps.text

if __name__ == '__main__':
    inData = '{"application_id": "hypecore_sit", "secret": "Dtm28qR%k"}'

    token = LoginClass().api_login(inData)
    inData =  """
            {"page_number": 1, "page_size": 10, "member_id": "1", "platform": "any", "filter_list": "any", "operation": "any" }
        """
    res = ProductClass().list_product(token, inData)
    print(res)