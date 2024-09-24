import pytest
import requests
@pytest.fixture(scope="session")
def get_access_token():
    URL = "https://api,weixin.qq.com/cgi-bin/token?""\\""grant_type=client_credential&appid=wx7002cc0a80&secret=903b6b342003a5a9"
    rep=requests.get(URL)
    return rep.json()["access_token"]