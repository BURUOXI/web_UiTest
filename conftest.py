"""conftest.py 文件名称是固定的。

统一存放 fixt    ure 的地方。
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True, scope= "class")
def get_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login():
    keys = "13385289600"
    keys2 = "123456Aa"
    # 打开谷歌浏览器，建立会话。启动Chromedriver.exe  打开Chrome
    driver = webdriver.Chrome()
    # 访问百度首页
    driver.get("https://locationpc.lanhanba.net/auth/login?CID=90")
    # 点击登录按钮
    sleep(2)
    driver.find_element_by_xpath('.//input[@placeholder="请输入手机号"]').send_keys(keys)
    driver.find_element_by_xpath('.//input[@placeholder="请输入密码"]').send_keys(keys2)
    driver.find_element_by_xpath('.//button[@class="el-button lhb-mt-34 el-button--primary"]').click()
    WebDriverWait(driver, 5).until(
        lambda x: x.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[5]/div[2]/button")).click()
    user = WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[3]")).text
    print(user)
    return user
