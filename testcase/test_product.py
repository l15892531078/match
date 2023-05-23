# author：xintian
# time:2020-06-17
#-*- coding: utf-8 -*-
from Lib.ApiLogin import LoginClass
from Lib.ApiProdcut import ProductClass
import json, os
import pytest
import allure
from Lib.GetExcelData import getExcelData
@allure.feature('课程模块')#一级标题
class TestProdoct:
    # 个性化商品推荐接口需要登录
    def setup_class(self):#登录
        """登录初始化"""
        self.token = LoginClass().api_login('{"application_id": "hypecore_sit", "secret": "Dtm28qR%k"}')
    # 1- 所有参数正常填写
    #fixtrue---参数化---excel
    @allure.story("个性化商品推荐接口")
    @allure.title("个性化商品用例")
    @pytest.mark.parametrize('inData,repsData', getExcelData(1, 1, 3, 6, 8))
    def test_add_lesson(self,inData,repsData):
        """商品推荐接口"""
        res = ProductClass().list_product(self.token,inData)
        assert  json.loads(res)['success'] ==  json.loads(repsData)['success']#断言



# if __name__ =="__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
#     pytest.main(['test_product.py','-s','--alluredir', '../report/tmp'])
#     # 执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
#     os.system('allure generate  ../report/tmp -o ../report/report --clean')

