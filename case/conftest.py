from selenium import webdriver
from pages.login_page import LoginPage
import time
import pytest


@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver'''
    _driver = webdriver.Chrome()
    _driver.maximize_window()  #窗口最大化

    def end():
        '''测试用例执行后，执行终结函数'''
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope='session')
def login(driver):
    '''前置：登陆'''
    web = LoginPage(driver)
    web.login()
    return driver
