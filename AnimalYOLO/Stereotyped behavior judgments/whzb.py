import math

# 读取数据并计算欧氏距离
def calculate_euclidean_distances(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # 假设每行的数据是以空格分隔的数字
    first_line_data = [float(x) for x in lines[0].strip().split()]
    distances = []

    for line in lines:
        line_data = [float(x) for x in line.strip().split()]
        x_min=line_data[0]
        y_min=line_data[1]
        x_max=line_data[2]
        y_max=line_data[3]
        w=x_max-x_min+1
        h=y_max-y_min+1
        b=w/h
        distances.append(b)

    # 将计算得到的欧氏距离写入文件
    with open(output_file, 'w') as file:
        i=0
        for distance in distances:
            file.write(f"{i} {distance}\n")
            i=i+1

# 调用函数
calculate_euclidean_distances(r'D:\桌面\蜂猴论文\刻板行为\data_make\moving_know\vid_1\group_3.0.txt', r'.\vid_1_3.txt')
