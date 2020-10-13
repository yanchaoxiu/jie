# -*- coding: utf-8 -*-
import datetime
import os

import win32com.client as win32

import jiekou.readConfig

read_conf = jiekou.readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
# app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
# addressee = read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
# cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
mail_path = os.path.join(jiekou.getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径



def send_mail():
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    mail.Recipients.Add('1822107818@qq.com')  # 收件人
    # mail.CC = cc  # 抄送
    mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
    mail.BodyFormat = 2
    mail.Attachments.Add(mail_path, 1, 1, "myFile")
    content = u"""
                执行测试中……
                测试已完成！！
                生成报告中……
                报告已生成……
                报告已邮件发送！！
                """
    mail.Body = content
    mail.Send()

if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(subject)
    send_mail()
    print("send email ok!!!!!!!!!!")
