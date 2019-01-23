# coding=utf-8
import time
import unittest
from parents.business.login_business import LoginBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class ParentsLoginCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_business = LoginBusiness(parames)

    def test_01(self):
        flag = self.login_business.login_password_error()
        time.sleep(2)
        self.assertTrue(flag, u"密码错误,登陆失败~")

    def test_02(self):
        flag = self.login_business.login_user_error()
        time.sleep(2)
        self.assertTrue(flag, u"用户名错误,登陆失败~")

    def test_03(self):
        self.login_business.login_pass()
        #self.assertTrue(flag, u"登录成功~")

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
