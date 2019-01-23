# coding=utf-8
from teacher.handle.notice_handle import NoticeHandle
from util.screenshot import Screenshots
import time


class NoticeBusiness:
    def __init__(self, driver):
        self.notice_handle = NoticeHandle(driver)
        self.content = str(time.time())
        self.screenshots = Screenshots(driver)

    def enter_send_notice(self):
        time.sleep(2)
        self.notice_handle.click_to_school()
        time.sleep(1)
        self.screenshots.saveScreenshot()
        time.sleep(2)
        self.notice_handle.click_create_notice()

    def send_notice_no_content(self):
        time.sleep(2)
        self.notice_handle.click_send_to()
        time.sleep(2)
        self.notice_handle.click_select_all()
        time.sleep(1)
        self.notice_handle.click_right_button()
        time.sleep(3)
        self.notice_handle.click_right_button()
        time.sleep(1)
        self.notice_handle.click_send_to()
        time.sleep(2)
        self.notice_handle.click_select_all()
        time.sleep(1)
        self.notice_handle.click_right_button()
        time.sleep(0.5)
        self.screenshots.saveScreenshot()

    def send_notice_no_obj(self):
        time.sleep(1)
        self.notice_handle.send_notice_content(self.content)
        time.sleep(3)
        self.notice_handle.click_right_button()
        time.sleep(1)
        self.notice_handle.clear_notice_content()
        time.sleep(0.5)
        self.screenshots.saveScreenshot()

    def send_notice_suss(self):
        time.sleep(2)
        self.notice_handle.click_send_to()
        time.sleep(2)
        self.notice_handle.click_select_all()
        time.sleep(1)
        self.notice_handle.click_right_button()
        time.sleep(1)
        self.notice_handle.send_notice_content(self.content)
        time.sleep(3)
        self.notice_handle.click_right_button()
        time.sleep(2)
        self.screenshots.saveScreenshot()

    def enter_school_notice(self):
        # time.sleep(2)
        # self.notice_handle.click_to_school()
        # time.sleep(2)
        # self.notice_handle.click_notice_for_title("学校通知")
        time.sleep(2)
        self.notice_handle.click_notice_for_content(self.content)
        time.sleep(2)
        self.screenshots.saveScreenshot()
        time.sleep(3)
        self.notice_handle.click_back_button()
        time.sleep(2)

    def back_to_homepage(self):
        time.sleep(2)
        self.notice_handle.click_back_button()
        time.sleep(2)
        self.notice_handle.click_back_to_homepage()
        time.sleep(2)
