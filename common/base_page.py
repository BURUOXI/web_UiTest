"""
存储每个页面的通用行为。

"""


import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Setting


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def screenshot(self):
        """保存截图
        时间戳
        """
        # 154332313.123
        # 文件名
        img_path = Setting.img_path
        filename = str(int(time.time())) + '.png'
        file = os.path.join(img_path, filename)
        self.driver.save_screenshot(file)
        return file

    def get_element(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
            return e
        except NoSuchElementException as e:
            logging.error("查找元素失败")
            self.screenshot()
            # 截图

    def wait_clickable_element(self, locator, timeout=60, poll=0.2):
        """等待元素可以被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.element_to_be_clickable(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("查找元素失败")
            self.screenshot()

    def wait_presence_element(self, locator, timeout=60, poll=0.2):
        """等待元素出现"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("查找元素失败")
            self.screenshot()

    def wait_visible_element(self, locator, timeout=60, poll=0.2):
        """等待元素可见"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.visibility_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("查找元素失败")
            self.screenshot()

    def input(self, name_prop, data):
        """全局文件输入，输入框
        e.send_keys()
        """
        e = self.driver.find_element_by_name(name_prop)
        e.send_keys(data)

    def click(self, locator):
        """click 点击"""
        e = self.wait_clickable_element(locator)
        e.click()


    def click_element(self, *loc):
        """
        重封装的click方法，将寻找和点击封装到一起，适用于点击次数不多的元素
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:None
        """
        try:
            webelement = self.driver.find_element(*loc)
            webelement.click()
        except (TimeoutException, NoSuchElementException) as e:
            print ('Error details :%s' % (e.msg))

    def rewrite_cases(self):
        """
        重构读取的数据

        """
        pass

    # 哪些方法是所有的页面共有的呢？？
    # 用户输入，
    # selector 操作
    # 切换， 窗口，frame, alert
    # 鼠标操作
    # 双击，悬停，右击
    # 窗口滑动（调用 js)
    # 上传文件
    # pytest 的使用




