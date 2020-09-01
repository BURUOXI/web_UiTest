from common.base_page import BasePage
from config import Setting


class CreatecompanyPage(BasePage):
    """注册公司页面"""
    url = '/enterprise/register/?curTab=1&CID=90'


    def get(self):
        """访问注册公司"""
        login_url = Setting.host + self.url
        self.driver.get(login_url)

    def raad_case(self):
        print("用例来了")