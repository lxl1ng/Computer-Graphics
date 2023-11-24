from many import *

xmin, ymin, xmax, ymax = -6, -6, 6, 6


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
        plt.plot(X, Y, color)
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
            plt.plot(X, Y, color)

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
            plt.plot(X, Y, color)

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
            plt.plot(X, Y, color)

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
            plt.plot(X, Y, color)


def creat_window(xmin, ymin, xmax, ymax, color):
    bresenham_change(xmin, ymin, xmax, ymin, color)
    bresenham_change(xmin, ymin, xmin, ymax, color)
    bresenham_change(xmin, ymax, xmax, ymax, color)
    bresenham_change(xmax, ymin, xmax, ymax, color)


def Cohen_Sutherland(x1, y1, x2, y2):
    # 判断直线是否在裁剪窗口内
    def inside(x, y):
        return xmin <= x <= xmax and ymin <= y <= ymax

    # 计算直线斜率
    if x2 - x1 == 0 or y2 - y1 == 0:
        print(1)
        if x2 - x1 == 0:
            print(2)
            if inside(x1, ymin):
                if y1 < ymin:
                    y1 = ymin
                if y2 > ymax:
                    y2 = ymax
                color = 'r'
                return x1, y1, x2, y2, color
            else:
                color = 'g'
                return x1, y1, x2, y2, color
        if y2 - y1 == 0:
            print(3)
            if inside(xmin, y1):
                if x1 < xmin:
                    x1 = xmin
                if x2 > xmax:
                    x2 = xmax
                color = 'r'
                return x1, y1, x2, y2, color
            else:
                color = 'g'
                return x1, y1, x2, y2, color

    else:
        k = (y2 - y1) / (x2 - x1)

        # 计算直线与裁剪窗口的交点
        def intersect(x1, y1, x2, y2, edge):
            if edge == "left":
                x = xmin
                y = y1 + k * (x - x1)
            elif edge == "right":
                x = xmax
                y = y1 + k * (x - x1)
            elif edge == "bottom":
                y = ymin
                x = x1 + (y - y1) / k
            elif edge == "top":
                y = ymax
                x = x1 + (y - y1) / k
            return x, y

        # 判断直线是否在裁剪窗口内
        if inside(x1, y1) and inside(x2, y2):
            color = 'r'
            return x1, y1, x2, y2, color

        # 计算直线与裁剪窗口的交点
        if x1 < xmin:
            x1, y1 = intersect(x1, y1, x2, y2, "left")
        if x2 > xmax:
            x2, y2 = intersect(x1, y1, x2, y2, "right")
        if y1 < ymin:
            x1, y1 = intersect(x1, y1, x2, y2, "bottom")
        if y2 > ymax:
            x2, y2 = intersect(x1, y1, x2, y2, "top")

        # 递归裁剪直线
        return Cohen_Sutherland(x1, y1, x2, y2)


grid()
plt.axis([-10, 10, -10, 10])
creat_window(xmin, ymin, xmax, ymax, 'b')

# 两头外
bresenham_change(-8, -8, 9, 9, 'g')
x1_clip, y1_clip, x2_clip, y2_clip,color = Cohen_Sutherland(-8, -8, 9, 9)
bresenham_change(x1_clip, y1_clip, x2_clip, y2_clip, color)

# 一头外
bresenham_change(-5, 5, 8, -5, 'g')
x1_clip, y1_clip, x2_clip, y2_clip, color = Cohen_Sutherland(-5, 5, 8, -5)
bresenham_change(x1_clip, y1_clip, x2_clip, y2_clip, color)

# 全外
bresenham_change(-9, -9, 9, -9, 'g')
x1_clip, y1_clip, x2_clip, y2_clip, color = Cohen_Sutherland(-9, -9, 9, -9)
bresenham_change(x1_clip, y1_clip, x2_clip, y2_clip, color)
bresenham_change(-9, -9, -9, 9, 'g')
x1_clip, y1_clip, x2_clip, y2_clip, color = Cohen_Sutherland(-9, -9, -9, 9)
bresenham_change(x1_clip, y1_clip, x2_clip, y2_clip, color)

# 全内
bresenham_change(-4, -5, 2, -2, 'g')
x1_clip, y1_clip, x2_clip, y2_clip,color = Cohen_Sutherland(-4, -5, 2, -2)
bresenham_change(x1_clip, y1_clip, x2_clip, y2_clip, color)


plt.show()
