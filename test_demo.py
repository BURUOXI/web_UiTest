# """pytest 的 parametrize 功能（ddt） 不能和 unittest 兼容。"""
#
#
#
# import unittest
# import pytest
# from selenium import webdriver
#
# test_data = [1,2,3]
#
# # 我是一个测试夹具 == 》 setUp
# @pytest.fixture(scope='module')
# def init_web():
#     """启动浏览器"""
#     print("前置置条件")
#     driver = webdriver.Chrome()
#
#     yield driver  # 暂停
#     print("后置条件")
#     driver.quit()
#
#
# class TestDemo:
#
#     @pytest.mark.parametrize("test_info", test_data)
#     @pytest.mark.demo
#     def test_demo(self, test_info, init_web):
#         pass
#
#
# class TestUser:
#     def test_user(self, init_web):
#         pass


