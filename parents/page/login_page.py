# coding=utf-8
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal


class LoginPage:
    # 获取登录页面所有的页面元素信息
    def __init__(self, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        # 获取用户名元素信息
        return self.get_by_local.get_element('username','parents_login_element')

    def get_password_element(self):
        # 获取密码元素信息
        return self.get_by_local.get_element('password', 'parents_login_element')

    def get_login_button_element(self):
        # 获取登陆按钮元素信息
        return self.get_by_local.get_element('login_button', 'parents_login_element')

    def get_forget_password_element(self):
        # 忘记密码元素
        return self.get_by_local.get_element('forget_password', 'parents_login_element')

    def get_register_element(self):
        # 注册元素
        return self.get_by_local.get_element('register', 'parents_login_element')

    def get_tost_element(self, message):
        # 获取tostelement
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))

    def get_mime_element(self):
        # 首页元素
        return self.get_by_local.get_element('mine', 'parents_login_element')

    def get_close_button_element(self):
        return self.get_by_local.get_element('close_button', 'parents_login_element')

    def get_learn_element(self, message):
        elements = self.get_by_local.get_element('learn_head', 'parents_login_element')
        learn_element = False
        for element in elements:
            if element.text == message:
                learn_element = element
                break
        print(learn_element.text)
        return learn_element

