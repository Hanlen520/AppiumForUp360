# coding=utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal


class NoticePage:
    # 获取登录页面所有的页面元素信息
    def __init__(self, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_school_element(self):
        # 获取家校元素信息
        return self.get_by_local.get_element('school', 'teacher_notice_element')

    def get_create_teacher_notice_element(self):
        # 获取通知元素信息
        return self.get_by_local.get_element('create_notice', 'teacher_notice_element')

    def get_notice_content_element(self):
        # 获取通知内容元素信息
        return self.get_by_local.get_element('notice_content', 'teacher_notice_element')

    def get_send_to_element(self):
        # 获取选择联系人元素信息
        return self.get_by_local.get_element('send_to', 'teacher_notice_element')

    def get_select_all_element(self):
        # 获取选择所有班级元素信息
        return self.get_by_local.get_element('select_all', 'teacher_notice_element')

    def get_tost_element(self, message):
        # 获取tostelement
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))

    def get_screenshot(self, file_name):
        # 截屏
        return self.screenshot.saveScreenshot(file_name)

    def get_right_button_element(self):
        # 获取确定按钮的元素信息
        return self.get_by_local.get_element('right_button', 'teacher_notice_element')

    def get_back_button_element(self):
        # 获取确定按钮的元素信息
        return self.get_by_local.get_element('back_button', 'teacher_notice_element')

    def get_notice_content(self):
        return self.get_by_local.get_element('content', 'teacher_notice_element')

    def get_notice_element_for_title(self, title):
        elements = self.get_by_local.get_element('notice_title', 'teacher_notice_element')
        teacher_notice_element = False
        for element in elements:
            if element.text == title:
                teacher_notice_element = element
                break
        return teacher_notice_element

    def get_notice_element_for_content(self, content):
        elements = self.get_by_local.get_element('content', 'teacher_notice_element')
        content_element = False
        for element in elements:
            if element.text == content:
                content_element = element
                break
        return content_element

    def get_homepage_element(self):
        # 获取选择联系人元素信息
        return self.get_by_local.get_element('home_page')


if __name__ == '__main__':
    notice = NoticePage()
    print(notice.get_notice_content())