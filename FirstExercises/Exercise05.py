# coding=utf-8
"""
Exercise 05
The code reads three coefficients a, b and c of quadratic equation
(ax2 + bx + c = 0, a ̸= 0) from STDIN and print it two roots.
"""
import math

a, b, c = map(float, input("Please enter a b c; a/=0\n").split(" "))
if a == 0:
    print("Invalid Input,a/=0")
else:
    # 计算判别式
    discriminant = b ** 2 - 4 * a * c

    # 根据判别式的值分类
    if discriminant > 0:
        # 两个不相同的实根
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Root 1:%.3f" % root1)
        print("Root 2:%.3f" % root2)
    elif discriminant == 0:
        # 两个相同的根
        root = -b / (2 * a)
        print("Root:%.3f" % root)
    else:
        # 复数根
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        print("Root 1:", root1)
        print("Root 2:", root2)
