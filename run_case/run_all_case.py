import pytest

"""
测试文件以test_开头或以_test结尾
测试类以Test开头，并且不能带有init方法
测试函数以test_开头
断言使用基本的assert
"""
if __name__ == '__main__':
    # pytest.main(['../test_case/test_case_01.py'])
    # pytest.main(['../test_case/test_case_01.py', '../test_case/test_case_02.py'])
    """
    1.生成html的报告
    '--html=../report/report.html'
    2.生成xml格式的报告
    '--junitxml=../report/report.xml'
    3.生成allure的报告
      a.生成allure结果目录
      '--alluredir','../report/reportallure'
      b.生成allure报告
         i.下载程序
         ii.解压、添加环境变量
         iii.执行命令 allure generate ./reportallure/ -o ./reporthtml/ --clean
    """
    pytest.main(['../test_case', '--html=../report/report.html', '--junitxml=../report/report.xml', '--alluredir','../report/reportallure'])