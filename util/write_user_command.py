# coding=utf-8
import yaml
import os


class WriteUserCommand:
    def __init__(self):
        config_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.config_file = config_dir + "//config//DevicesConfig.yaml"

    def read_data(self):
        '''
        加载yaml数据
        '''
        data = {}
        with open(self.config_file) as fr:
            data = yaml.load(fr)
        print(data)
        return data

    def get_value(self, key, port):
        '''
        获取value
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        '''
        写入数据
        '''
        data = self.join_data(i, device, bp, port)
        with open(self.config_file, "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(self.config_file, "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        try:
            cnt = len(data)
        except TypeError:
            cnt = 0
        return cnt


if __name__ == '__main__':
    write_file = WriteUserCommand()
