# coding=utf-8
from parents.handle.article_handle import ArticleHandle
from util.screenshot import Screenshots
import time


class ArticleBusiness:
    def __init__(self, driver):
        self.article_handle = ArticleHandle(driver)
        self.screenshots = Screenshots(driver)
        self.driver = driver

    def access_article(self):
        time.sleep(5)
        self.article_handle.click_article_tab()
        time.sleep(10)
        self.article_handle.click_article()
        time.sleep(15)
        cons = self.driver.contexts  # 获取上下文列表
        self.driver._switch_to.context(cons[1])
        self.driver.context
        print(self.driver.page_source)
        print(self.driver.find_element_by_class_name('article-title').text)
        print(self.driver.current_context)
        self.driver.press_keycode('4')
        time.sleep(5)
        self.driver._switch_to.context(cons[0])
        print(self.driver.current_context)
