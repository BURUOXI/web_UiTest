# """投资用例。
#
# 前置条件：
# 1，登录
# 2，有余额。充值，1， 无法进行web自动化充值。 2， 直接修改数据库； 3，接口充值。4，手工充值
# 充多少钱？？
# 1， 每次查看用例你需要投资多少钱，我就充值多少（每次执行用例之前，都需要去充值一次）
# 2， 先充一个亿。
#
# 3，有项目可投
#
#
# 投资流程：
# 1，首页点击投标。
# 2， 投标详情页
#
# """
# import unittest
# from decimal import Decimal
#
# import ddt
# from selenium import webdriver
#
# from config.user_config import User
# from pages.home_page import HomePage
# from pages.invest_page import InvestPage
# from pages.login_page import LoginPage
# from pages.user_page import UserPage
#
# test_money = [100]
#
# @ddt.ddt
# class TestInvest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         # 登录
#         self.driver = webdriver.Chrome()
#         # 设置隐式等待
#         wait_timeout = 20
#         self.driver.implicitly_wait(wait_timeout)
#         LoginPage(self.driver).login(User.username, User.pwd)
#         # 进入用户界面，获取余额
#         # self.money_before = ''
#
#     def tearDown(self) -> None:
#         self.driver.quit()
#
#     @ddt.data(*test_money)
#     def test_invest_success(self, money):
#         """投资成功用例"""
#         HomePage(self.driver).click_invest_btn()
#         invest_page = InvestPage(self.driver)
#         # 投标， 得到投标之前的余额
#         money_before = invest_page.bid(money)
#
#         # 点击投标成功
#         # invest_page.active_success()
#         # self.assertEqual(invest_page.get_bid_success().text, '投标成功！')
#
#         # self.assertIn('投标成功', invest_page.get_bid_success().text)
#         self.assertTrue( "投标成功" in invest_page.get_bid_success().text )
#
#         # 点击投标成功
#         invest_page.active_success()
#         # 投资之后的余额
#         money_after = UserPage(self.driver).get_money()
#         # 断言
#         # 使用 Decimal 进行浮点数运算
#         # Decimal 当中传递的参数类型是字符串，不是浮点数，也不是整形。
#         assert Decimal(money_before) - Decimal(str(money)) == Decimal(money_after)
#
#
#         # 要判断余额
#         # 坑1：浮点数 断言。丢失精度， 0。1 + 0.2 != 0.3
#         # 坑2： 余额之前  - 投资金额 == 之后余
#         # BasePage, 截图，log记录， 异常处理
