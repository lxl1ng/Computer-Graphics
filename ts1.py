from many import *


def DDA(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    X = [x1, x2]
    Y = [y1, y2]
    if dx == 0:
        grid()
        plt.axis([0, 10, 0, 10])
        x, y = x1, y1
        # 绘点
        t = 0
        for i in range(0, int(abs(dy) + 1)):
            # 需要四舍五入
            plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
            plt.savefig("./img/" + str(i) + '.png')
            if dy > 0:
                y += 1
            else:
                y -= 1
            t += 1
        plt.plot(X, Y)
        plt.savefig('./img/' + str(int(round(t))) + '.png')
    else:
        k = dy / dx
        if 1 >= k > 0:
            grid()
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                x += 1
                y += float(k)
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k > 1:
            grid()
            k = 1 / k
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                y += 1
                x += float(k)
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(y))) + '.png')

        if 0 >= k > -1:
            grid()
            plt.axis([0, 10, -5, 5])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                x += 1
                y += float(k)
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k < -1:
            grid()
            k = 1 / k
            plt.axis([0, 10, -10, 0])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                # 需要四舍五入
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                y -= 1
                x -= float(k)
            plt.plot(X, Y)
            plt.savefig('./img/' + str(-int(round(y))) + '.png')


def mid_point(x1, y1, x2, y2):
    # Ax+By+C=0
    dx, dy = x2 - x1, y2 - y1
    X = [x1, x2]
    Y = [y1, y2]
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    if dx == 0:
        grid()
        plt.axis([-10, 10, -10, 10])
        x, y = x1, y1
        # 绘点
        t = 0
        for i in range(0, int(abs(dy) + 1)):
            # 需要四舍五入
            plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
            plt.savefig("./img/" + str(i) + '.png')
            if dy > 0:
                y += 1
            else:
                y -= 1
            t += 1
        plt.plot(X, Y)
        plt.savefig('./img/' + str(int(round(t))) + '.png')
    else:
        k = dy / dx
        if 1 >= k > 0:
            d = 2 * (-dy) + dx
            d1 = 2 * (-dy)
            d2 = 2 * ((-dy) + dx)
            grid()
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                if d < 0:
                    x += 1
                    y += 1
                    d += d2
                else:
                    x += 1
                    y = y
                    d += d1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k > 1:
            d = 2 * (-dx) + dy
            d1 = 2 * (-dx)
            d2 = 2 * ((-dx) + dy)
            grid()
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                if d < 0:
                    x += 1
                    y += 1
                    d += d2
                else:
                    y += 1
                    x = x
                    d += d1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(y))) + '.png')

        if 0 >= k > -1:
            d = -dx - 2 * dy
            d1 = -2 * dx - 2 * dy
            d2 = -2 * dy
            grid()
            plt.axis([0, 10, -5, 5])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                if d < 0:
                    x += 1
                    y = y
                    d += d2
                else:
                    x += 1
                    y -= 1
                    d += d1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k < -1:
            d = -dy - 2 * dx
            d1 = -2 * dx
            d2 = -2 * dy - 2 * dx
            grid()
            plt.axis([0, 10, -10, 0])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                if d < 0:
                    x += 1
                    y -= 1
                    d += d2
                else:
                    y -= 1
                    x = x
                    d += d1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(-int(round(y))) + '.png')


def bresenham(x1, y1, x2, y2):
    # Ax+By+C=0
    dx, dy = x2 - x1, y2 - y1
    X = [x1, x2]
    Y = [y1, y2]
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    if dx == 0:
        grid()
        plt.axis([-10, 10, -10, 10])
        x, y = x1, y1
        # 绘点
        t = 0
        for i in range(0, int(abs(dy) + 1)):
            # 需要四舍五入
            plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
            plt.savefig("./img/" + str(i) + '.png')
            if dy > 0:
                y += 1
            else:
                y -= 1
            t += 1
        plt.plot(X, Y)
        plt.savefig('./img/' + str(int(round(t))) + '.png')
    else:
        k = dy / dx
        e = -0.5
        if 1 >= k > 0:
            grid()
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                x += 1
                e = e + k
                if e >= 0:
                    y += 1
                    e -= 1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k > 1:
            grid()
            k = 1 / k
            plt.axis([0, 10, 0, 10])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                y += 1
                e = e + k
                if e >= 0:
                    x += 1
                    e -= 1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(y))) + '.png')

        if 0 >= k > -1:
            grid()
            plt.axis([0, 10, -5, 5])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dx) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                x += 1
                e = e - k
                if e >= 0:
                    y -= 1
                    e -= 1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(int(round(x))) + '.png')

        if k < -1:
            grid()
            k = 1 / k
            plt.axis([0, 10, -10, 0])
            x, y = x1, y1
            # 绘点
            for i in range(0, int(abs(dy) + 1)):
                plt.plot(int(round(x)), int(round(y)), 'r*', markersize=7)
                plt.savefig("./img/" + str(i) + '.png')
                y -= 1
                e = e - k
                if e >= 0:
                    x += 1
                    e -= 1
            plt.plot(X, Y)
            plt.savefig('./img/' + str(-int(round(y))) + '.png')


# bresenham(0,0,0,7)
# # 0<k<1:
# mid_point(1, 1, 8, 6)
# # k>1:
# bresenham(1, 0, 7, 10)
# # 0>k>-1:
# mid_point(0, 1, 7, 1)
# # k<-1:
bresenham(1, 0, 5, -7)
plt.show()
# to_gif()
# show_gif()
