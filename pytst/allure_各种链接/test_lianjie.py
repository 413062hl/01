import allure
import pytest
test_case_link="https://cn.bing.com/search?q=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&cvid=92ec06759f5940d39c41c6eb2e86120a&aqs=edge.0.69i59j0l8.1784j0j8&FORM=ANSPA1&PC=U531"
@allure.link("www.baidu.com")
def test_01():
    pass
@allure.link("www.qq音乐.com",name="单击进入")
def test_with_named_link():
    pass
@allure.issue("https://y.qq.com/","测试出现的问题")
def test_issue_link():
    pass
@allure.testcase(test_case_link,"测试登录")
def test_case_link():
    pass
