import pytest
import os
import shutil


if __name__ == '__main__':
    if os.path.exists('report/'):
        shutil.rmtree('report/')

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
    pytest.main(['./testcase/test_product.py', '-s', '--alluredir', './report/tmp'])
    # 执行命令 allure generate ./report/tmp -o ./report --clean ，生成测试报告
    os.system('allure generate  ./report/tmp -o ./report/report --clean')