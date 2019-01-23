# coding=utf-8
import yaml
import os
import codecs


class HandleFile:
    def __init__(self):
        config_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.config_file = config_dir + "//config//login.java"
        self.data = []

    def read_data(self):
        with codecs.open(self.config_file, encoding='utf-8') as fr:
            lines = fr.readlines()
            for line in lines:
                line = line.strip().replace("\r\n", "")
                if line.startswith('@Xpath') or line.startswith('@Description'):
                    print(line)
                    self.data.append(line)
                else:
                    continue
        fr.close()
        return self.data

    def clear_data(self):
        with codecs.open(self.config_file, "w") as fr:
            fr.truncate()
        fr.close()

    def write_data(self, file_data):
        with open(self.config_file, "a") as fr:
            fr.write('\r\n'.join(file_data))


if __name__ == '__main__':
    handle_file = HandleFile()
    data = handle_file.read_data()

    #handle_file.clear_data()
    #handle_file.write_data(data)
