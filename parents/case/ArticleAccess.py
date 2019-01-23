# coding=utf-8
import time
import unittest
from parents.business.article_business import ArticleBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class ParentsArticleCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.article_business = ArticleBusiness(parames)

    def access_article(self):
        self.article_business.access_article()

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
