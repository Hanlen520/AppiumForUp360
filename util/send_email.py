# -*- coding:utf-8 -*
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from util.read_init import ReadIni
import smtplib
import os


class Email:
    def __init__(self):
        config_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path = config_dir + "//config//EmailConfig.ini"
        self.read_ini = ReadIni(file_path)

    # ---发送邮件---
    def send_email(self, file_name, report_file):
        # 创建一个带附件的实例
        msg = MIMEMultipart()

        # 配置SMTP服务器
        smtp_server = self.read_ini.get_value("smtp_server", "Email")
        username = self.read_ini.get_value("username", "Email")
        password = self.read_ini.get_value("password", "Email")

        # 发件人和收件人
        sender = self.read_ini.get_value("sender", "Email")
        to_list = self.read_ini.get_value("to_list", "Email")
        to_list = to_list.split(',')

        # 定义邮件头
        msg['From'] = sender
        msg['To'] = ";".join(to_list)
        msg["Subject"] = u"up360自动化测试报告"

        # 定义邮件正文
        content = "请从附件下载测试报告并查看"
        content = MIMEText(content, _subtype='html', _charset='utf-8')
        msg.attach(content)

        # 定义邮件附件
        file = MIMEText(open(report_file, 'rb').read(), 'base64', 'gb2312')
        file["Content-Type"] = 'application/octet-stream'
        file["Content-Disposition"] = 'attachment; filename=' + file_name  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(file)

        # 发送邮件
        try:
            server = smtplib.SMTP()
            server.connect(smtp_server)
            server.login(username, password)
            server.sendmail(sender, to_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    email = Email()
    if email.send_email("debug.log", "F:\\debug.log"):
        print("发送成功")
    else:
        print("发送失败")
