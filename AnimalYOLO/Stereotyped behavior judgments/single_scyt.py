'''import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def read_data_and_plot(file_path):
    # 从文件中读取数据
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析数据
    time_points = [float(line.split()[0]) for line in lines]
    value1 = [float(line.split()[1]) for line in lines]
    value2=[value1[:lis[0]],value1[lis[0]:lis[1]],value1[lis[1]:lis[2]],value1[lis[2]:lis[3]],value1[lis[3]:]]
    #value2=[value1]
    for y in value2:
        x=[]
        for i in range(len(y)):
            x.append(i)

        x = np.array(x)
        y = np.array(y)
        # 创建三次样条插值对象
        cs = CubicSpline(x, y)

        # 生成插值点
        x_new = np.linspace(x.min(), x.max(), 100)
        y_new = cs(x_new)

        # 绘制原始数据点
        plt.scatter(x, y, color='red', label='Original Data')

        # 绘制三次样条插值曲线
        plt.plot(x_new, y_new, label='Cubic Spline Interpolation')

        # 设置图表标题和图例
        plt.title('Cubic Spline Interpolation of Time Series Data')
        plt.legend()

        # 显示图表
        plt.show()

# 调用函数并传入文件路径
file_path = r'D:\刻板行为\data_make\moving_know\wh\video_23_6.txt'  # 替换为你的数据文件路径
lis=[21,96,166,181]
read_data_and_plot(file_path)'''

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import os

def read_data_and_plot(file_path, output_folder):
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 从文件中读取数据
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析数据
    time_points = [float(line.split()[0]) for line in lines]
    value1 = [float(line.split()[1]) for line in lines]
    value2 = [value1[:lis[0]], value1[lis[0]:lis[1]], value1[lis[1]:lis[2]], value1[lis[2]:lis[3]], value1[lis[3]:]]
    #value2 = [value1]
    for idx, y in enumerate(value2):
        x = []
        for i in range(len(y)):
            x.append(i)

        x = np.array(x)
        y = np.array(y)
        # 创建三次样条插值对象
        cs = CubicSpline(x, y)

        # 生成插值点
        x_new = np.linspace(x.min(), x.max(), 100)
        y_new = cs(x_new)

        # 绘制原始数据点
        plt.scatter(x, y, color='red', label='Original Data')

        # 绘制三次样条插值曲线
        plt.plot(x_new, y_new, label='Cubic Spline Interpolation')

        # 设置图表标题和图例
        plt.title('Cubic Spline Interpolation of Time Series Data')
        plt.legend()

        # 将图像保存到输出文件夹
        plt.savefig(os.path.join(output_folder, f'scyt_{idx+1}.png'))

        # 关闭图像以防止在下一个图像中使用
        plt.close()


# 调用函数并传入文件路径和输出文件夹路径
videoname=23
videoid=6
'''file_path = f'D:\刻板行为\data_make\moving_know\wh\\video_{videoname}_{videoid}.txt'  # 替换为你的数据文件路径
output_folder = f'D:\刻板行为\data_make\moving_know\\new_wh\\video_{videoname}_{videoid}'  # 替换为你想要保存图片的文件夹路径'''
file_path = r"D:\桌面\蜂猴论文\Animal总\zbanimal\video_8_1.txt"
output_folder=r"D:\桌面\Animal总\animalsss\video_8_1"
lis = [101,171,196,291]
read_data_and_plot(file_path, output_folder)
