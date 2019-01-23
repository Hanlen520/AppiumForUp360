# coding=utf-8
import time
import os
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.read_init import ReadIni


class BaseDriver:
    def android_driver(self, i, type):
        print("this is android_driver:", i)
        # devices_name adb devices
        write_file = WriteUserCommand()
        ini_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        read_ini = ReadIni(ini_dir + "//config/ApplyConfig.ini")

        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        apk_name = read_ini.get_value("apk", type)
        appPackage = read_ini.get_value("package_name", type)
        appWaitActivity = read_ini.get_value("activity", type)
        noReset = read_ini.get_value("noReset", type)

        capabilities = {
            "platformName": "Android",
            # "automationName":"UiAutomator2",
            "deviceName": devices,
            "app": apk_name,
            "appWaitActivity": appWaitActivity,
            "noReset": noReset,
            "platforVersion": "4.4.4",
            "appPackage": appPackage,
            # "chromedriverExecutableDir": ini_dir + "\config\chromedriver\webview",
            'recreateChromeDriverSessions': True

        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        time.sleep(10)
        return driver
