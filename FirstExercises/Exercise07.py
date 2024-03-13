# coding=utf-8
"""
Exercise 07
 Print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on
creation of patterns.) Different sizes of alphabet rangoli are shown below:
#size 3         size 4
            ------d------
----c----   ----d-c-d----
--c-b-c--   --d-c-b-c-d--
c-b-a-b-c   d-c-b-a-b-c-d
--c-b-c--   --d-c-b-c-d--
----c----   ----d-c-d----
            ------d------

Author: Shen Zhengdong
"""
import string

# 导入string模块以获取小写字母字符
pattern = string.ascii_lowercase

# 获取用户输入的rangoli的大小
n = int(input("请输入大小：\n"))

L = []
for i in range(n):
    # 创建一个由字符通过"-"分隔的字符串，从第i个字符到最后一个字符
    s = "-".join(pattern[i:n])
    # 将字符串反转并将其与原始字符串（不包括第一个字符）连接起来
    # 得到的字符串将是每行的图案
    pattern_line = s[::-1] + s[1:]
    # 将图案居中在长度为(4 * n - 3)且填充"-"的字符串中
    centered_pattern = pattern_line.center(4 * n - 3, "-")
    # 将居中的图案添加到列表L中
    L.append(centered_pattern)

# 将L中的图案按照逆序（不包括第一个图案）使用换行符连接起来，
# 然后打印结果
print('\n'.join(L[:0:-1] + L))
