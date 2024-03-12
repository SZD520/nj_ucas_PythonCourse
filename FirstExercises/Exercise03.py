# coding=utf-8
"""
Exercise 03
Find emails in a text, split username and mail server
"""
import re
text = input("Enter a text: \n")
# 定义电子邮件的正则表达式模式
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# 使用正则表达式查找文本中的电子邮件
emails = re.findall(email_pattern, text)

# 遍历找到的电子邮件列表
for email in emails:
    # 使用字符串分割操作分离用户名和邮件服务器
    username, mail_server = email.split('@', 1)

    # 打印用户名和邮件服务器
    print("Email:", email)
    print("Username:", username)
    print("Mail Server:", mail_server)
    print()
