# coding=utf-8
from teacher.pages.notice_page import NoticePage


class NoticeHandle:
    def __init__(self, driver):
        self.notice_page = NoticePage(driver)

    # 操作登录页面的元素
    def send_notice_content(self, content):
        '''
        输入通知内容
        '''
        self.notice_page.get_notice_content_element().send_keys(content)

    def clear_send_to(self):
        '''
        点击跳转到选择联系人
        '''
        self.notice_page.get_send_to_element().clear()

    def clear_notice_content(self):
        '''
        输入通知内容
        '''
        self.notice_page.get_notice_content_element().clear()

    def click_to_school(self):
        '''
        点击家校按钮
        '''
        self.notice_page.get_school_element().click()

    def click_create_notice(self):
        '''
        点击跳转发送通知页面
        '''
        self.notice_page.get_create_teacher_notice_element().click()

    def click_send_to(self):
        '''
        点击跳转到选择联系人
        '''
        self.notice_page.get_send_to_element().click()

    def click_select_all(self):
        '''
        点击跳转到选择联系人
        '''
        self.notice_page.get_select_all_element().click()

    def click_right_button(self):
        '''
        点击确定或者发送按钮
        '''
        self.notice_page.get_right_button_element().click()

    def click_back_button(self):
        '''
        点击确定或者发送按钮
        '''
        self.notice_page.get_back_button_element().click()

    def get_fail_tost(self, message):
        '''
        获取tost，根据返回信息进行反数据
        '''
        tost_element = self.notice_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False

    def get_notice_content(self):
        content = self.notice_page.get_notice_content()
        if content:
            return content
        else:
            return False

    def click_notice_for_title(self, title):
        self.notice_page.get_notice_element_for_title(title).click()

    def click_notice_for_content(self, content):
        self.notice_page.get_notice_element_for_content(content).click()

    def click_back_to_homepage(self):
        self.notice_page.get_homepage_element().click()
