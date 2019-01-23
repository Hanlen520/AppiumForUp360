# coding=utf-8
from teacher.pages.homework_page import HomeworkPage


class HomeworkHandle:
    def __init__(self, driver):
        self.homework_page = HomeworkPage(driver)

    def click_to_homework(self):
        '''
        点击进入作业模块
        '''
        self.homework_page.get_homework_tab_element().click()

    def click_to_publish(self):
        '''
        点击进入布置模块
        '''
        self.homework_page.get_homework_publish_element().click()

    def click_to_subject(self, subject):
        '''
        点击某个具体科目
        '''
        self.homework_page.get_subject_element(subject).click()

    def click_to_homework_publish(self, homework_name):
        '''
        点击某个具体作业
        '''
        self.homework_page.get_homework_element(homework_name).click()

    def click_back_to_homepage(self):
        '''
        返回APP首页
        '''
        self.homework_page.get_homepage_element().click()