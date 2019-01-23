# coding=utf-8
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal


class ArticlePage:
    # 获取登录页面所有的页面元素信息
    def __init__(self, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_article_tab_element(self):
        #
        return self.get_by_local.get_element('article', 'parents_article_element')

    def get_article_element(self):
        elements = self.get_by_local.get_element('article_title', 'parents_article_element')
        return elements[1]

    def get_icon_back_element(self):
        return self.get_by_local.get_element('icon_back', 'parents_article_element')
