# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal


class HomeworkPage:
    def __init__(self, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    # 返回首页
    def get_homepage_element(self):
        # 获取首页的原素信息
        return self.get_by_local.get_element('home_page')

    # 获取作业tab
    def get_homework_tab_element(self):
        return self.get_by_local.get_element('homework_tab', 'teacher_homework_element')

    # 获取布置作业按钮
    def get_homework_publish_element(self):
        return self.get_by_local.get_element('homework_publish', 'teacher_homework_element')

    # 获取科目
    def get_subject_element(self, subject):
        elements = self.get_by_local.get_element('subject_tab', 'teacher_homework_element')
        subject_element = False
        for element in elements:
            if element.text == subject:
                subject_element = element
                break
        return subject_element

    # 获取作业
    def get_homework_element(self, homework_name):
        elements = self.get_by_local.get_element('homework', 'teacher_homework_element')
        homework_element = False
        for element in elements:
            if element.text == homework_name:
                homework_element = element
                break
        return homework_element

