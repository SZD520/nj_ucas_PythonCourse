# coding=utf-8
"""
Exercise 02
You are given a string. Split the string on a “ ” (whitespace) delimiter and then
join them using hyphens (“-”). i.e.:
I Have a Dream! → [’I', ’Have’, ’a’, ’Dream!’] → I-Have-a-Dream!
"""
# 用户输入一个字符串
string = input("Enter a string: \n")

# 使用空格分割字符串并创建一个字符串列表
stringList = string.split(" ")

# 打印分割后的字符串列表
print("Split string:\n", stringList)

# 检查字符串列表的长度
if len(stringList) < 2:
    # 如果列表长度小于2，说明只有一个单词，直接打印原字符串
    print("Converted string:\n" + string)
else:
    # 如果列表长度大于等于2，说明有多个单词
    string = stringList[0]  # 取第一个单词作为初始字符串

    # 遍历列表中的其他单词
    for index in range(1, len(stringList)):
        stringList[index] = "-" + stringList[index]  # 在每个单词前加上"-"
        string += stringList[index]  # 将修改后的单词添加到字符串中

    # 打印修改后的字符串
    print("Converted string:\n" + string)