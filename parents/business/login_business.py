# coding=utf-8
from parents.handle.login_handle import LoginHandle
from util.screenshot import Screenshots
import time


class LoginBusiness:
    def __init__(self, driver):
        self.login_handle = LoginHandle(driver)
        self.screenshots = Screenshots(driver)
        self.driver = driver

    def login_pass(self):
        self.login_handle.send_username('13867429835')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()
        time.sleep(10)
        #self.login_handle.click_close()
        #time.sleep(5)
        #self.login_handle.click_close()
        #time.sleep(5)
        #flag = self.login_handle.get_mine_text()
        #time.sleep(1)
        self.screenshots.saveScreenshot()
        time.sleep(5)
        #self.login_handle.click_learn_head('24点')
        #time.sleep(5)
        #for cons in self.driver.contexts:
            #print(cons)
            #if cons.lower().startswith("webview"):
                #self.driver._switch_to.context(cons)
                #break

        #if flag:
            #return True
        #else:
            #return False

    def login_user_error(self):
        self.login_handle.send_username('13067429835')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()
        time.sleep(1)
        self.screenshots.saveScreenshot()
        user_flag = self.login_handle.get_fail_tost('帐号未注册')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('13867429835')
        self.login_handle.send_password('654321')
        self.login_handle.click_login()
        time.sleep(1)
        self.screenshots.saveScreenshot()
        user_flag = self.login_handle.get_fail_tost('登陆密码错误')
        if user_flag:
            return True
        else:
            return False
