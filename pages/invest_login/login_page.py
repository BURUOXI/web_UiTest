"""

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config import Setting
from common.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    """登录页面"""
    url = 'auth/login?CID=90'

    user_locator = (By.XPATH, './/input[@placeholder="请输入手机号"]')
    pwd_locator = (By.XPATH, './/input[@placeholder="请输入密码"]')
    btn_locator = (By.XPATH, './/button[@class="el-button lhb-mt-34 el-button--primary"]')
    # 获取输入手机号提示语
    prompt_user = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[1]/div/div[2]')
    # 获取请输入密码提示语
    prompt_pwd = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]')
    # 登录成功-选择账号
    login_success = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]')
    # error_info_locator = (By.XPATH, ".//button[@class="el-button lhb-mt-34 el-button--primary"]")
    invalid_info_toast = (By.CLASS_NAME, '/html/body/div[6]/p')


    def get(self):
        """访问登录页面"""
        login_url = Setting.host + self.url
        self.driver.get(login_url)

    def login(self, username, pwd):
        """登录操作"""
        self.get()
        sleep(5)
        # 定位用户名
        user_elem = self.get_element(self.user_locator)
        # 3， 输入用户名；
        user_elem.send_keys(username)

        # 4， 定位密码；
        pwd_elem = self.get_element(self.pwd_locator)
        # 5, 输入密码
        pwd_elem.send_keys(pwd)
        # 6, 定位登录按钮；
        self.get_element(self.btn_locator).click()
        # 7,点击登录按钮；

    def get_ver_required(self):
        """验证必填项"""
        ver_required_user = self.wait_visible_element(self.prompt_user)
        ver_required_pwd = self.wait_visible_element(self.prompt_pwd)
        # print(ver_required_user)
        return ver_required_user.text


    def get_error_msg(self):
        """获取手机号为空"""
        error_elem = self.wait_visible_element(self.prompt_user)
        # print(error_elem)
        return error_elem.text

    def get_invalid_msg(self):
        """获取密码为空"""
        invalid_elem = self.wait_visible_element(self.prompt_pwd)
        # print(invalid_elem)
        return invalid_elem.text

    def choose_account_num(self):
        """选择账号进入首页"""
        account_num = self.wait_visible_element(self.login_success)  # 使用等待元素出现的方法
        # print(account_num)
        return account_num.text

    def get_toast_msg(self):
        tosat_msg = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(By.XPATH,"/html/body/div[6]/p")).text
        # 这里使用原生的，使用封装的轮询时间太长，toast已经消失掉了
        # print(tosat_msg)
        return tosat_msg


