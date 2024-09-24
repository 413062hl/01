import allure
import pytest
def test_01():
    pass
@allure.severity(allure.severity_level.MINOR)
@allure.title("等级为minor")
@allure.link("https://www.qq.com/",name="qq企鹅")
def test_02():
    pass
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("等级为block")
def test_03():
    pass