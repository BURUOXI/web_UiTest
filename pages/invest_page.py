# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from common.base_page import BasePage
#
#
# class InvestPage(BasePage):
#
#     # 投标输入框
#     bid_input_locator = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")
#     bid_btn_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
#     # 投标成功元素
#     bid_success_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")
#     # 激活按钮元素
#     bid_success_active_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")
#
#     def get_bid_input(self):
#         """获取投标输入框元素"""
#         e = self.get_element(self.bid_input_locator)
#         return e
#
#     def get_bid_btn(self):
#         """获取投标按钮元素"""
#         e = self.get_element(self.bid_btn_locator)
#         return e
#
#     def bid(self, money):
#         """投标.
#         返回投标之前的余额： type: str
#         """
#         input_element = self.get_bid_input()
#         # 获取余额属性 data-amount
#         money_before = input_element.get_attribute('data-amount')
#         input_element.send_keys(money)
#         self.get_bid_btn().click()
#         return money_before
#
#     def active_success(self):
#         """点击投资成功并激活"""
#         # e = self.driver.find_element(*self.bid_success_active_locator)
#         e = WebDriverWait(self.driver, 20).until(
#             EC.element_to_be_clickable(self.bid_success_active_locator)
#         )
#         # 强制等待（0.1）
#         e.click()
#
#     def get_bid_success(self):
#         e = self.get_element(self.bid_success_msg_locator)
#         return e
#
#
