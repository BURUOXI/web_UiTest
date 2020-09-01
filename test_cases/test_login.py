"""测试登录功能。

流程：
1，启动浏览器，打开url;
2, 定位用户名；
3， 输入用户名；
4， 定位密码；
5， 输入密码；
6， 定位登录按钮；
7， 点击登录按钮；
8，定位错误信息断言
"""
import pytest

from data import login_data_success, login_data_error,login_data_num_error,login_data_invalid
# from pages.home_page import HomePage
from pages.invest_login.login_page import LoginPage



class TestLogin:


    @pytest.mark.parametrize('test_info', login_data_num_error)
    def test_login_invalid_user(self, test_info, get_browser):
        """密码为空"""
        driver = get_browser
        expected = test_info['expected']
        # print(expected)
        LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
        invalid_msg = LoginPage(driver).get_invalid_msg()
        # print(invalid_msg)
        try:
            assert invalid_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', login_data_error)
    def test_login_username_empty(self, test_info, get_browser):
        """用户名为空"""
        driver = get_browser
        expected = test_info['expected']
        # print(expected)
        LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
        error_msg = LoginPage(driver).get_error_msg()
        # print(error_msg)
        try:
            assert error_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', login_data_invalid)
    def test_login_error(self, test_info, get_browser):
        """用户名或者密码错误"""
        driver = get_browser
        expected = test_info['expected']
        LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
        toast_msg = LoginPage(driver).get_toast_msg()
        try:
            assert toast_msg == expected
        except AssertionError as e:
            raise e
    #
    # @pytest.mark.smoke
    # def test_login_success_user(self, test_info, init_web,get_browser):
    #     driver = get_browser
    #     expected = test_info['expected']
    #     LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
    #     account_msg = HomePage(driver).get_user_info()
    #     try:
    #         assert account_msg == expected
    #     except AssertionError as e:
    #         raise e

    @pytest.mark.parametrize('test_info', login_data_success)
    def test_login_success(self, test_info, get_browser):
        """正常登陆成功"""
        driver = get_browser
        expected = test_info['expected']
        # print(expected)
        LoginPage(driver).login(test_info["mobile"], test_info["pwd"])
        correct_msg = LoginPage(driver).choose_account_num()
        # print(correct_msg)
        try:
            assert correct_msg == expected
        except AssertionError as e:
            raise e


