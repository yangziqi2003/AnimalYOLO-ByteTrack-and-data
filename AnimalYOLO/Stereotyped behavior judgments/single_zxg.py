'''import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import numpy as np
import matplotlib.pyplot as plt
from single_fly import file_path
from single_scyt import *

def autocorrelation_coefficient(data, lag):
  mean = np.mean(data)
  n = len(data)
  r = np.sum((data[i] - mean) * (data[i - lag] - mean) for i in range(lag,n)) / np.sum((data[i] - mean) * (data[i] - mean) for i in range(n))
  return r

with open(file_path, 'r') as file:
    lines = file.readlines()

# 解析数据
time_points = [float(line.split()[0]) for line in lines]
value1 = [float(line.split()[1]) for line in lines]
value2 = [value1[:lis[0]], value1[lis[0]:lis[1]], value1[lis[1]:lis[2]], value1[lis[2]:lis[3]], value1[lis[3]:]]
#value2=[value1]
j=1
for y in value2:
    x = []
    for i in range(len(y)):
        x.append(i)

    x = np.array(x)
    y = np.array(y)
    data=y
    # 计算不同延迟时间的自相关系数
    lags = range(len(data))
    autocorr_coeffs = [autocorrelation_coefficient(data, lag) for lag in lags]

    # 绘制柱状图
    plt.bar(range(len(autocorr_coeffs)), autocorr_coeffs)
    # 设置标题和坐标轴标签
    plt.title(f"Graph of the autocorrelation coefficient for the period{j}")
    plt.xlabel("Lag")
    plt.ylabel("AFC")
    # 显示图表
    plt.show()
    j=j+1'''

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import numpy as np
import matplotlib.pyplot as plt
from single_fly import file_path
from single_scyt import *
import os

def autocorrelation_coefficient(data, lag):
    mean = np.mean(data)
    n = len(data)
    r = np.sum((data[i] - mean) * (data[i - lag] - mean) for i in range(lag, n)) / np.sum((data[i] - mean) * (data[i] - mean) for i in range(n))
    return r

def save_plots(data_series, output_folder):
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    j = 1
    for y in data_series:
        x = []
        for i in range(len(y)):
            x.append(i)

        x = np.array(x)
        y = np.array(y)
        data = y
        # 计算不同延迟时间的自相关系数
        lags = range(len(data))
        autocorr_coeffs = [autocorrelation_coefficient(data, lag) for lag in lags]

        # 绘制柱状图
        plt.bar(range(len(autocorr_coeffs)), autocorr_coeffs)
        # 设置标题和坐标轴标签
        plt.title(f"Graph of the autocorrelation coefficient for the period{j}")
        plt.xlabel("Lag")
        plt.ylabel("AFC")

        # 保存图表到输出文件夹
        plt.savefig(os.path.join(output_folder, f'autocorr_plot_{j}.png'))

        # 关闭图表以防止重复使用
        plt.close()

        j += 1

# 使用代码
with open(file_path, 'r') as file:
    lines = file.readlines()

# 解析数据
time_points = [float(line.split()[0]) for line in lines]
value1 = [float(line.split()[1]) for line in lines]
value2 = [value1[:lis[0]], value1[lis[0]:lis[1]], value1[lis[1]:lis[2]], value1[lis[2]:lis[3]], value1[lis[3]:]]
#value2=[value1]
save_plots(value2, output_folder)
