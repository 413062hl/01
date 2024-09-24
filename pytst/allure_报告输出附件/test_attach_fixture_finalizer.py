import allure
import pytest
@pytest.fixture()
def attach_file_in_module_scope_fixture_with_finalizer():
    allure.attach("C:\hai\123.jpg","嵇海亮最棒",allure.attachment_type.JPG)
    # def finailer_moule_scope_fixture():
    #     allure.attach("这个文本是文件级别的结束部分","下面调用finializer",allure.attachment_type.TEXT)
    # reuqest.addfinalizer(finailer_moule_scope_fixture)
def test(attach_file_in_module_scope_fixture_with_finalizer):
    print("这是通过fixture调用上面的步骤，步骤包含结束finalizer的调用")

    pass
@pytest.fixture()
def attach_file():
    allure.attach.file("C:\hai\\123.jpg","嵇海亮最棒",allure.attachment_type.JPG)
def test01(attach_file):
    print("zuibang")