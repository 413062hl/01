import allure
import pytest
@allure.title("测试上下电")
def test_01():
    assert 2+2==4
@allure.title("测试常稳：")
def test_02():
    assert 3+3==6

@allure.title("参数化标题：{param1} with param2")
@pytest.mark.parametrize("param1,param2,expected",[(2,2,4),(1,2,5)])
def test_03(param1,param2,expected):
    assert param2+param1==expected
@allure.title("动态标题")
def test_04():
    assert 2+2==4
    allure.dynamic.title("测试基础软件")