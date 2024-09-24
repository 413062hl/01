import allure
import pytest
import requests
def accen_token():
    URL="https://api,weixin.qq.com/cgi-bin/token?"
    rep=requests.get(URL)
    assert 200==rep.status_code
    rep_json=rep.json()
    assert 7200==rep_json["expires_in"]
    assert rep.elapsed.total_seconds()<3
    return rep_json["access_token"]
#创建正确的标签用例
def test_createdtag():
    URL="https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+accen_token()
    data={"tag":{"name":"000"}}
    rep=requests.post(URL=URL,json=data)
    assert 200==rep.status_code
    json_rep=rep.json()
    assert "000"==json_rep["tag"]["name"]
#创建错误的用例7
def test_createtag_f_erroetoken():
    URL = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=1111"
    rep=requests.get(URL)
    assert 200==rep.status_code
    assert 40001==rep.json()["errcode"]
if __name__ == '__main__':
    pytest.main(["-vs","test_create_tag"])