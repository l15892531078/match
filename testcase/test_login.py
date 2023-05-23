import allure, pytest, json, os
from Lib.ApiLogin import LoginClass
from Lib.GetExcelData import getExcelData


@allure.feature('登录模块')
@allure.story('登录接口')
@allure.title('登录接口用例')
@allure.severity('critical')
@pytest.mark.parametrize('inData, respData', getExcelData(0, 1, 2, 6, 8))
def test_login(inData, respData):
    """
    登录操作
    :param inData:
    :param respData:
    :return:
    """
    resp = LoginClass().api_login(inData, getSession=False)
    resp_code = json.loads(resp)
    excel_code = json.loads(respData)

    assert resp_code['success'] == excel_code['success']


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
    pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp'])
    # # 执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
    os.system('allure generate  ../report/tmp -o ../report/report --clean')