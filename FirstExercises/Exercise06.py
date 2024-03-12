# coding=utf-8
"""
Exercise 06
The user enters a string and a substring. Find the number of times that the
substring occurs in the given string. String traversal will take place from left to
right, not from right to left. i.e.:
Print the text in a string’, ’in’
the result should be 3.
"""
# 用户输入一个字符串
string = input("Enter a string: \n")

# 用户输入一个子字符串
substring = input("Enter a substring: \n")

# 计数子字符串在字符串中出现的次数
num_occurrences = 0

# 使用循环查找子字符串
while True:
    try:
        # 在字符串中查找子字符串的索引
        index = string.index(substring, 0, len(string) - 1)

        # 找到子字符串，计数加一
        num_occurrences += 1

        # 更新字符串为从子字符串后的部分开始
        string = string[index + 1:]
    except ValueError:
        # 没有找到子字符串，退出循环
        break

# 打印子字符串在字符串中出现的次数
print("The number is %d" % num_occurrences)

