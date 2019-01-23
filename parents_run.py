# coding=utf-8

import unittest
import time
import os
import sys
import multiprocessing
import threading
import HTMLTestRunner
from util.server import Server
from util.get_case_list import GetCaseList
from util.write_user_command import WriteUserCommand
from base.base_driver import BaseDriver
from parents.case.ParentsLogin import ParentsLoginCase
from parents.case.ArticleAccess import ParentsArticleCase
from util.send_email import Email

sys.path.append("..")


def get_driver(i):
    base_driver = BaseDriver()
    driver = base_driver.android_driver(i, "Parents")
    return driver


# 获取测试用例集
def create_suite(i):
    # 定义单元测试容器
    suite = unittest.TestSuite()
    driver = get_driver(i)

    case_list = GetCaseList()
    data = case_list.get_value('P', 'case_list_'+str(i))
    if len(data) > 0:
        for case in data:
            methods = case['method']
            case_name = case['caseName']
            for method in methods.split(','):
                suite.addTest(eval(case_name)(method, parame=driver))
    else:
        return None
    return suite


# 运行测试用例
def get_suite(i):
    suite = create_suite(i)

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    file_path = os.getcwd() + "\\report\\report\\" + day + "\\parents"

    file_name = now + "-" + str(i) + "_result.html"
    if os.path.exists(file_path):
        file_path = file_path + "\\" + file_name
    else:
        os.makedirs(file_path)
        file_path = file_path + "\\" + file_name

    fp = open(file_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'向上网家长端端自动化测试报告', description=u'用例执行情况:')
    runner.run(suite)
    fp.close()

    Email.send_email(file_name, file_path)

# 获取测试设备数量
def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


# 启动服务
def appium_init():
    server = Server()
    server.main("parents")


# 停止服务
def appium_stop():
    server = Server()
    server.kill_server()


# 判断线程是否存活
def get_thread_status(threads):
    status = False
    for thread in threads:
        if thread.is_alive():
            status = True
            break
    return status


if __name__ == '__main__':
    # 启动服务
    appium_init()

    # 获取测试设备数
    cnt = get_count()

    # 配置线程
    global threads
    threads = []
    if cnt:
        for i in range(cnt):
            t = multiprocessing.Process(target=get_suite, args=(i,))
            # t = threading.Thread(target=get_suite, args=(i,))
            threads.append(t)

        # 启动线程
        for j in threads:
            j.start()
            time.sleep(10)

        # 线程结束则停止服务
        while get_thread_status(threads):
            time.sleep(5)
            print("线程还活着，不要杀掉服务啊~")
        else:
            appium_stop()
    else:
        print("木有找到测试设备~")
