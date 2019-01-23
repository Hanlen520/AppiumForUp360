# coding=utf-8
import yaml
import os

class GetCaseList:
    def __init__(self):
        self.config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def read_data(self, type):
        '''
        加载yaml数据
        '''
        if type == 'T':
            file_name = self.config_path+"/config/TeacherCaseList.yaml"
        elif type == 'P':
            file_name = self.config_path+"/config/ParentsCaseList.yaml"

        with open(file_name) as fr:
            data = yaml.load(fr)
        return data

    def get_value(self, type, key):
        '''
        获取value
        '''
        data = self.read_data(type)
        value = data[key]
        return value


if __name__ == '__main__':
    write_file = GetCaseList()
    data = write_file.get_value('T', 'case_list_0')
    if len(data) > 0:
        for case in data:
            methods = case['method']
            case_name = case['caseName']
            print(methods, case_name)