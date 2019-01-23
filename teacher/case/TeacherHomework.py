# coding=utf-8
import unittest
from time import sleep
from teacher.business.homework_business import HomeworkBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global driver
        driver = parame


class TeacherHomeworkCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.homework_business = HomeworkBusiness(driver)

    def publish_homework(self):
        self.homework_business.enter_homework_page()
        self.homework_business.enter_publish()
        self.homework_business.choose_subject("语文")
        self.homework_business.enter_homework("同步作业")

    def back_to_homepage(self):
        self.homework_business.back_to_homepage()

    def tearDown(self):
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        sleep(1)
