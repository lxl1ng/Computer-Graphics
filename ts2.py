from many import *


def circlepoints(xc, yc, x, y):
    plt.plot(int(round(xc + x)), int(round(yc + y)), 'r.', markersize=7)
    plt.plot(int(round(xc + x)), int(round(yc - y)), 'r.', markersize=7)
    plt.plot(int(round(xc - x)), int(round(yc + y)), 'r.', markersize=7)
    plt.plot(int(round(xc - x)), int(round(yc - y)), 'r.', markersize=7)
    plt.plot(int(round(xc + y)), int(round(yc + x)), 'r.', markersize=7)
    plt.plot(int(round(xc + y)), int(round(yc - x)), 'r.', markersize=7)
    plt.plot(int(round(xc - y)), int(round(yc + x)), 'r.', markersize=7)
    plt.plot(int(round(xc - y)), int(round(yc - x)), 'r.', markersize=7)


def ellipticpoints(xc, yc, x, y):
    plt.plot(int(round(xc + x)), int(round(yc + y)), 'r.', markersize=7)
    plt.plot(int(round(xc + x)), int(round(yc - y)), 'r.', markersize=7)
    plt.plot(int(round(xc - x)), int(round(yc + y)), 'r.', markersize=7)
    plt.plot(int(round(xc - x)), int(round(yc - y)), 'r.', markersize=7)


def mid_pointcircle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    i = 0
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    grid()
    plt.axis([xc - 10, xc + 10, yc - 10, yc + 10])
    plt.plot(xc, yc, 'b.', markersize=7)
    circlepoints(xc, yc, x, y)
    plt.savefig("./img/" + str(0) + '.png')
    while x <= y:
        if d < 0:
            d += (2 * x) + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        i += 1
        circlepoints(xc, yc, x, y)
        plt.savefig("./img/" + str(i) + '.png')


def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    i = 0
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    grid()
    plt.axis([xc - 10, xc + 10, yc - 10, yc + 10])
    plt.plot(xc, yc, 'b.', markersize=7)
    circlepoints(xc, yc, x, y)
    plt.savefig("./img/" + str(0) + '.png')
    while x < y:
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
        i += 1
        circlepoints(xc, yc, x, y)
        plt.savefig("./img/" + str(i) + '.png')


def mid_pointelliptic(xc, yc, a, b):
    x = 0
    y = b
    d1 = b * b - a * a * b + a * a / 4
    dx = 4 * b * b * x
    dy = 4 * a * a * y
    i = 0
    # 横纵坐标轴
    plt.xlabel('X')
    plt.ylabel('Y')
    grid()
    plt.axis([xc - 10, xc + 10, yc - 10, yc + 10])
    plt.plot(xc, yc, 'b.', markersize=7)
    ellipticpoints(xc, yc, x, y)
    plt.savefig("./img/" + str(0) + '.png')
    while dx < dy:
        if d1 < 0:
            dx += 4 * b * b
            d1 += dx + 2 * b * b
        else:
            y -= 1
            dx += 4 * b * b
            dy -= 4 * a * a
            d1 += dx - dy + 2 * b * b
        x += 1
        i += 1
        ellipticpoints(xc, yc, x, y)
        plt.savefig("./img/" + str(i) + '.png')
    d2 = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    while y > 0:
        if d2 > 0:
            dy -= 4 * a * a
            d2 += a * a - dy
        else:
            x += 1
            dx += 4 * b * b
            dy -= 4 * a * a
            d2 += dx - dy + 2 * a * a
        y -= 1
        i += 1
        ellipticpoints(xc, yc, x, y)
        plt.savefig("./img/" + str(i) + '.png')


clear_files()
# mid_pointcircle(1,3,7)
# bresenham_circle(0, 0, 7)
mid_pointelliptic(1, 1, 4, 7)
# to_gif()
# show_gif()
plt.show()