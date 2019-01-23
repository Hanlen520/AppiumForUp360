# coding=utf-8
from parents.page.article_page import ArticlePage


class ArticleHandle:
    def __init__(self, driver):
        self.article_page = ArticlePage(driver)
        self.driver = driver

    # 操作登录页面的元素
    def click_article_tab(self):
        self.article_page.get_article_tab_element().click()

    def click_article(self):
        element = self.article_page.get_article_element()
        element.click()

    def click_back_native(self):
        self.article_page.get_icon_back_element().click()