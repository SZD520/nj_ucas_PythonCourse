# coding=utf-8
"""
Exercise 01
 You are given a string and your task is to swap cases. In other words, convert all
lowercase letters to uppercase letters and vice versa. i.e.:
I Have a Dream! → i hAVE A dREAM!
"""

# 用户输入一个字符串
string = input('Enter a string: \n')

# 使用 swapcase() 方法将字符串中的大小写进行转换
string = string.swapcase()

# 打印转换后的字符串
print("Converted string:\n" + string)
