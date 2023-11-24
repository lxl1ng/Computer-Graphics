import glob
import os
import imageio
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
from matplotlib.ticker import MultipleLocator


def to_gif():
    filenames = glob.glob('./img/*.png')  # 遍历文件夹下的图片,注意后缀
    filenames = sorted(filenames, key=lambda x: int((os.path.basename(x).split('.')[0]).split('_')[-1]))
    # 转化的GIF图片名称
    save_name_gif = "cp.gif"

    # fps 就是图片切换的频率，越大越快。也可以使用duration参数来控制，表示每帧间隔，单位s
    fps = 3

    # 播放次数，0表示循环播放，1表示播放1次，2表示播放2次，以此类推
    loop = 0

    # 存放图片的列表
    pics_list = []

    # 遍历filenames,使用imageio读取后存入pics_list
    for image_name in filenames:
        im = imageio.imread(image_name)
        pics_list.append(im)

        # 生成gif
    imageio.mimsave(save_name_gif, pics_list, fps=fps, loop=loop)


def show_gif():
    # 创建一个窗口
    window = tk.Tk()

    # 加载GIF动画
    gif = Image.open('cp.gif')

    # 创建一个标签
    label = tk.Label(window)
    label.pack()

    # 获取GIF动画的每一帧
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame_tk = ImageTk.PhotoImage(frame)
        frames.append(frame_tk)

    # 更新标签的图像以实现动画效果
    def update_label(index):
        frame = frames[index]
        label.configure(image=frame)
        window.after(300, update_label, (index + 1) % len(frames))

    # 开始动画
    update_label(0)

    # 运行窗口的主循环
    window.mainloop()


def clear_files():
    for file in glob.glob('./img/*'):
        os.remove(file)


def grid():
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    ax.set_aspect(1.0)
    plt.grid()
