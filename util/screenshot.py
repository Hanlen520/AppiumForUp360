# coding=utf-8
import os
import time
import logging


class Screenshots:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    # savePngName:生成图片的名称
    def getPngName(self):
        """
        name：自定义图片的名称
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        #fp = os.path.dirname(os.getcwd()) +"/report/screenshots/"+ day
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        fp = path +"/report/screenshots/" + day
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            file_name = fp + "\\" + tm + type
        else:
            os.makedirs(fp)
            file_name = fp + "\\" + tm + type

        return file_name

    # 获取系统当前时间
    def saveTime(self):
        """
        返回当前系统时间以括号中（2014-08-29-15_21_55）展示
        """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    # saveScreenshot:通过图片名称，进行截图保存
    def saveScreenshot(self):
        """
        快照截图
        name:图片名称
        """
        # 获取当前路径
        file_name = self.getPngName()
        try:
            self.driver.get_screenshot_as_file(file_name)
            print(file_name)
        except NameError as e:
            print("Failed to take screenshots! %s" % e)

        return file_name
