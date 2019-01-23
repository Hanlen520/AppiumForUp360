# coding=utf-8
from teacher.handle.homework_handle import HomeworkHandle
from util.screenshot import Screenshots
import time


class HomeworkBusiness:
    def __init__(self, driver):
        self.homework_handle = HomeworkHandle(driver)
        self.screenshots = Screenshots(driver)

    def enter_homework_page(self):
        self.homework_handle.click_to_homework()
        time.sleep(1)
        self.screenshots.saveScreenshot()
        time.sleep(2)

    def enter_publish(self):
        self.homework_handle.click_to_publish()
        self.screenshots.saveScreenshot()
        time.sleep(2)

    def choose_subject(self, subject):
        self.homework_handle.click_to_subject(subject)
        self.screenshots.saveScreenshot()
        time.sleep(2)

    def enter_homework(self, homework_name):
        self.homework_handle.click_to_homework_publish(homework_name)
        self.screenshots.saveScreenshot()
        time.sleep(2)

    def back_to_homepage(self):
        self.homework_handle.click_back_to_homepage()
        time.sleep(2)
