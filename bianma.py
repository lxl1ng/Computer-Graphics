from many import *
from collections import Counter
import numpy as np

left = 4
right = 4
top = 4
low = -4


def bresenham_change(x1, y1, x2, y2, color):
    # Ax+By+C=0
    dx, dy = x2 - x1, y2 - y1
    X = [x1, x2]
    Y = [y1, y2]
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    if dx == 0:
        x, y = x1, y1
        # 绘点
        t = 0
        for i in range(0, int(abs(dy) + 1)):
            # 需要四舍五入
            plt.plot(int(round(x)), int(round(y)), '*', c=color, markersize=7)
            if dy > 0:
                y += 1
            else:
                y -= 1
            t += 1
        plt.plot(X, Y)
    else:
        k = dy / dx
        e = -0.5
        if 1 >= k > 0:
            x, y = x1, y1
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), '*', c=color, markersize=7)
                x += 1
                e = e + k
                if e >= 0:
                    y += 1
                    e -= 1
            plt.plot(X, Y)

        if k > 1:
            k = 1 / k
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), '*', c=color, markersize=7)
                y += 1
                e = e + k
                if e >= 0:
                    x += 1
                    e -= 1
            plt.plot(X, Y)

        if 0 >= k > -1:
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), '*', c=color, markersize=7)
                x += 1
                e = e - k
                if e >= 0:
                    y -= 1
                    e -= 1
            plt.plot(X, Y)

        if k <= -1:
            k = 1 / k
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), '*', c=color, markersize=7)
                y -= 1
                e = e - k
                if e >= 0:
                    x += 1
                    e -= 1
            plt.plot(X, Y)


def creat_window():
    bresenham_change(-4, -4, 4, -4, 'b')
    bresenham_change(-4, -4, -4, 4, 'b')
    bresenham_change(-4, 4, 4, 4, 'b')
    bresenham_change(4, 4, 4, -4, 'b')


def judge_code(x1, y1, x2, y2):
    code_begin = 0
    code_end = 0
    flag = 0
    if x1 < left:
        code_begin += 1
    if x1 > right:
        code_begin += 2
    if y1 < low:
        code_begin += 4
    if y1 > top:
        code_begin += 8
    if x2 < left:
        code_end += 1
    if x2 > right:
        code_end += 2
    if y2 < low:
        code_end += 4
    if y2 > top:
        code_end += 8

    code_judge1, code_judge2 = bin(code_begin | code_end)[2:].zfill(4), bin(code_begin & code_end)[2:].zfill(4)
    if code_judge1 == '0000':
        flag = 1
    if code_judge2 != '0000':
        flag = 2
    return flag


def Cohen_Sutherland_line(flag):
    if flag == 1:
        creat_window()
        bresenham_change(-7, 7, 7, -7, 'r')
        plt.show()


clear_files()
grid()
plt.axis([-10, 10, -10, 10])
# creat_window()
bresenham_change(-7, 7, 7, -7, 'r')
flag = judge_code(7, 7, 7, -7)
plt.show()
