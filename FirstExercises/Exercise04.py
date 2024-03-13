# coding=utf-8
"""
Exercise 04
Read a given string, change the character at a given index and then print the
modified string.
Sample Input
STDIN Function
----- --------
ABCDE s = 'ABCDE'
2 x position = 2, character = 'x'
Output
ABxD

Author: Shen Zhengdong
"""
# 用户输入一个字符串
string = input("Enter a string: \n")

# 用户输入一个位置和一个字符，使用空格分割
position, character = input("Enter a position and character: \n").split(" ")

# 检查字符是否超过一个字符
if len(character) > 1:
    print("Invalid character")
else:
    # 将位置转换为整数
    position = int(position)

    # 检查位置是否超出字符串范围
    if position > len(string)-1 or position < 0:
        print("Invalid position!")
    else:
        # 在指定位置替换字符
        new_string = string[:position] + character + string[position + 1:]

        # 打印替换后的字符串
        print("Converted string:\n"+new_string)