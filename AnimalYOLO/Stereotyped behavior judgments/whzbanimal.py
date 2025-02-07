# 导入所需的库
import math

# 读取数据并计算列之间的差异
def calculate_column_difference(input_file, output_file, delimiter=','):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    differences = []

    for line in lines:
        # 假设每行的数据是以逗号分隔的
        line_data = line.strip().split(delimiter)
        # 提取第五和第六列，假设它们是数字
        try:
            col5 = float(line_data[4])
            col6 = float(line_data[5])
            difference = col5 / col6
            differences.append(difference)
        except (IndexError, ValueError):
            # 如果列索引超出范围或数据无法转换为浮点数，跳过该行
            print(f"Error processing line: {line.strip()}")
            continue

    # 将计算得到的差异写入文件
    with open(output_file, 'w') as file:
        for i, difference in enumerate(differences):
            file.write(f"{i} {difference}\n")

# 调用函数
calculate_column_difference(r"D:\桌面\animals\video_9\1.0.txt", r"D:\桌面\zbanimals\video_9_1.txt")
