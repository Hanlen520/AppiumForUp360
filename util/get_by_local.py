# coding=utf-8
from util.read_init import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section=None):
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'ids':
                    return self.driver.find_elements_by_id(local_by)
                elif by == 'classNames':
                    return self.driver.find_elements_by_class_name(local_by)
                elif by == 'css':
                    return self.driver.find_element_by_css_selector(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None

    def get_element_by_type(self, type, value):
        if value != None:
            try:
                if type == 'id':
                    return self.driver.find_element_by_id(value)
                elif type == 'className':
                    return self.driver.find_element_by_class_name(value)
                elif type == 'ids':
                    return self.driver.find_elements_by_id(value)
                elif type == 'classNames':
                    return self.driver.find_elements_by_class_name(value)
                elif type == 'css':
                    return self.driver.find_element_by_css_selector(value)
                else:
                    return self.driver.find_element_by_xpath(value)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None
