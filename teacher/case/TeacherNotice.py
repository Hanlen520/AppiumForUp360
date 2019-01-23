# coding=utf-8
import unittest
from time import sleep
from teacher.business.notice_business import NoticeBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global driver
        driver = parame


class TeacherNoticeCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.notice_business = NoticeBusiness(driver)

    def enter_send_notice(self):
        self.notice_business.enter_send_notice()

    def send_notice(self):
        self.notice_business.send_notice_suss()

    def send_notice_no_content(self):
        self.notice_business.send_notice_no_content()

    def send_notice_no_obj(self):
        self.notice_business.send_notice_no_obj()

    def enter_notice(self):
        self.notice_business.enter_school_notice()

    def back_to_homepage(self):
        self.notice_business.back_to_homepage()

    def tearDown(self):
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        sleep(1)
