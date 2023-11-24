from collections import Counter
import numpy as np
from many import *

point = np.zeros((21, 21))
counter = Counter()
stack = []


def DDA_change(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    X = [x1, x2]
    Y = [y1, y2]
    if dx == 0:
        plt.axis([-10, 10, -10, 10])
        x, y = x1, y1
        # 绘点
        t = 0
        for i in range(0, int(abs(dy) + 1)):
            # 需要四舍五入
            point[round(x)][round(y)] = 1
            plt.plot(int(round(x)), int(round(y)), 'b*', markersize=7)
            if dy > 0:
                y += 1
            else:
                y -= 1
            t += 1
        plt.plot(X, Y)
    else:
        k = dy / dx
        if 1 >= k > 0:
            plt.axis([-10, 10, -10, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                point[round(x)][round(y)] = 1
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'b*', markersize=7)
                x += 1
                y += float(k)
            plt.plot(X, Y)

        if k > 1:
            k = 1 / k
            plt.axis([-10, 10, -10, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                point[round(x)][round(y)] = 1
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'b*', markersize=7)
                y += 1
                x += float(k)
            plt.plot(X, Y)

        if 0 >= k > -1:
            plt.axis([-10, 10, -10, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                point[round(x)][round(y)] = 1
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'b*', markersize=7)
                x += 1
                y += float(k)
            plt.plot(X, Y)

        if k <= -1:
            k = 1 / k
            plt.axis([-10, 10, -10, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                point[round(x)][round(y)] = 1
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'b*', markersize=7)
                y -= 1
                x -= float(k)
            plt.plot(X, Y)


def drow_lines():
    DDA_change(0, -10, 3, -3)
    DDA_change(-3, -3, 0, -10)
    DDA_change(-10, 0, -3, -3)
    DDA_change(3, -3, 10, 0)
    DDA_change(-10, 0, -3, 3)
    DDA_change(3, 3, 10, 0)
    DDA_change(-3, 3, 0, 1)
    DDA_change(0, 1, 3, 3)
    # 打孔
    DDA_change(-2, -1, 0, -3)
    DDA_change(0, -3, 2, -1)
    DDA_change(-2, -1, 2, -1)


def seed_fill(x, y):
    if point[x][y] == 0:
        point[x][y] = 1
        plt.plot(x, y, 'r.', markersize=7)
        i = sum(counter.values())
        plt.savefig("./img/" + str(i) + '.png')
        counter.update('1')
        if point[x + 1][y] == 0:
            seed_fill(x + 1, y)
        if point[x][y + 1] == 0:
            seed_fill(x, y + 1)
        if point[x - 1][y] == 0:
            seed_fill(x - 1, y)
        if point[x][y - 1] == 0:
            seed_fill(x, y - 1)


def seed_linefill(x, y):
    # 图形空白点入栈
    if point[x][y] == 0:
        stack.append((x, y))
        plt.plot(x, y, 'r.', markersize=7)
        i = sum(counter.values())
        plt.savefig("./img/" + str(i) + '.png')
        counter.update('1')
        while len(stack) != 0:
            # 栈顶像素出栈
            seed = stack.pop()
            x, y = seed
            # 从种子点像右边填充
            while point[x][y] == 0:
                point[x][y] = 1
                plt.plot(x, y, 'r.', markersize=7)
                x = x + 1
            right = x - 1  # 最👉位
            # 回到种子点
            x, y = seed
            x = x - 1
            # 向种子点左边填充
            while point[x][y] == 0:
                point[x][y] = 1
                plt.plot(x, y, 'r.', markersize=7)
                x = x - 1
            left = x + 1  # 最👈位
            # 处理上一条扫描线
            x = left
            y = y + 1
            while x <= right:
                flag = False
                while point[x][y] == 0:
                    flag = True
                    x = x + 1
                if flag:
                    stack.append((x - 1, y))
                    plt.plot(x - 1, y, 'g.', markersize=7)
                    flag = False
                while point[x][y] != 0 and x <= right:
                    x = x + 1
            # 处理下一条扫描线
            x = left
            y = y - 2
            while x <= right:
                flag = False
                while point[x][y] == 0:
                    flag = True
                    x = x + 1
                if flag:
                    stack.append((x - 1, y))
                    plt.plot(x - 1, y, 'g.', markersize=7)
                    flag = False
                while point[x][y] != 0 and x <= right:
                    x = x + 1
            i = sum(counter.values())
            plt.savefig("./img/" + str(i) + '.png')
            counter.update('1')


clear_files()
grid()
drow_lines()
# seed_fill(0, 0)
seed_linefill(0, -4)
print(point)
# to_gif()
# show_gif()
