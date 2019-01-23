import os
import time

'''
基本的adb操作
'''
class AndroidDebugBridge(object):
    # 执行adb命令
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result


    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        flag = [device for device in devices if len(device) > 2]
        if flag:
            return True
        else:
            return False
            # return [device for device in devices if len(device) > 2]

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result


    # 打开指定app
    def open_app(self,package_name, activity):
        result = self.call_adb("shell am  start -W -n %s/%s" % (package_name, activity))
        check = result.partition('\n')[2]
        # [2].replace('\n', '').split('\t ')
        if check.find("Error") >= 1:
            return False
        else:
            return True

    # 关闭指定app
    def close_app(self, package_name):
        result = self.call_adb("shell am force-stop %s" % package_name)
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 安装指定app
    def install_app(self, file_name, apk_name, push_dir="/data/local/tmp/", ):
        self.push(file_name, push_dir)
        time.sleep(5)
        result = self.call_adb("shell pm install %s" % push_dir+apk_name)
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell \" ps | grep "+pkg_name + "\"")
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        return result[5]

    # 关闭指定进程
    def close_app_pid(self, pkg_name):
        pid = self.get_app_pid(pkg_name)
        if not pid:
            return
        self.call_adb("shell \" kill " + pid + "\"")
        return

    # 卸载指定APP
    def uninstall_app(self, pkg_name):
        pid = self.get_app_pid(pkg_name)
        if not pid:
            return
        result = self.call_adb("uninstall  %s" % pkg_name)
        check = result.partition('\n')
        if check[0].find("Success") >= 1:
            return False
        else:
            return True

    # 卸载指定设备的指定APP
    def uninstall_app_for_device(self, devices_name,pkg_name):
        pid = self.get_app_pid(pkg_name)
        if not pid:
            return
        result = self.call_adb(" -s %s uninstall  %s" % (devices_name, pkg_name))
        check = result.partition('\n')
        if check[0].find("Success") >= 1:
            return False
        else:
            return True

