'''import numpy as np
from single_scyt import *


def estimate_top_positive_frequencies_periods_from_file(file_path):
    # 从文件中读取数据
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析数据
    time_points = [float(line.split()[0]) for line in lines]
    value1 = [float(line.split()[1]) for line in lines]
    value2=[value1[:lis[0]],value1[lis[0]:lis[1]],value1[lis[1]:lis[2]],value1[lis[2]:lis[3]],value1[lis[3]:]]
    #value2 = [value1]
    # 执行傅里叶变换
    for values in value2:
        fft_result = np.fft.fft(values)
        frequencies = np.fft.fftfreq(len(values), d=(time_points[1] - time_points[0]))
        # 仅保留正频率信息
        positive_frequencies_indices = np.where(frequencies > 0)[0]
        positive_frequencies = frequencies[positive_frequencies_indices]
        positive_fft_result = fft_result[positive_frequencies_indices]

        # 排序正频率的绝对值
        sorted_indices = np.argsort(np.abs(positive_fft_result))
        # 选择前五个正频率
        top_positive_frequencies_indices = positive_frequencies_indices[sorted_indices[-1:]]
        top_positive_frequencies_periods = 1 / frequencies[top_positive_frequencies_indices]
        print(top_positive_frequencies_periods)


# 示例：估计前五个正频率的周期
# 请将以下路径替换为您的文本文件路径
estimate_top_positive_frequencies_periods_from_file(file_path)'''

import numpy as np
from single_scyt import *
import os

periods_data=[]
def estimate_top_positive_frequencies_periods_from_file(file_path,output_folder):
    # 从文件中读取数据
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析数据
    time_points = [float(line.split()[0]) for line in lines]
    value1 = [float(line.split()[1]) for line in lines]
    value2=[value1[:lis[0]],value1[lis[0]:lis[1]],value1[lis[1]:lis[2]],value1[lis[2]:lis[3]],value1[lis[3]:]]
    #value2 = [value1]
    # 执行傅里叶变换
    for values in value2:
        fft_result = np.fft.fft(values)
        frequencies = np.fft.fftfreq(len(values), d=(time_points[1] - time_points[0]))
        # 仅保留正频率信息
        positive_frequencies_indices = np.where(frequencies > 0)[0]
        positive_frequencies = frequencies[positive_frequencies_indices]
        positive_fft_result = fft_result[positive_frequencies_indices]

        # 排序正频率的绝对值
        sorted_indices = np.argsort(np.abs(positive_fft_result))
        # 选择前五个正频率
        top_positive_frequencies_indices = positive_frequencies_indices[sorted_indices[-1:]]
        top_positive_frequencies_periods = 1 / frequencies[top_positive_frequencies_indices]
        periods_data.append(top_positive_frequencies_periods)

        # 将前五个正频率的周期保存到文本文件
        with open(os.path.join(output_folder, f'top_positive_frequencies_periods.txt'), 'w') as f:
            for period in periods_data:
                f.write(f'{period}\n')
        f.close()

estimate_top_positive_frequencies_periods_from_file(file_path, output_folder)

