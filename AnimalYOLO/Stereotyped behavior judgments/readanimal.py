# 导入所需的库
import os

# 读取文件并分类数据
def classify_and_write_data(file_path, videoname, delimiter=','):
    # 存储数据的字典，以ID为键
    data_dict = {}

    # 读取文件
    with open(file_path, 'r') as file:
        for line in file:
            # 去除行尾的换行符并分割字符串
            parts = line.strip().split(delimiter)
            frame = parts[0]
            id = parts[1]
            # 将整个行添加到对应的ID列表中
            if id not in data_dict:
                data_dict[id] = []
            data_dict[id].append(line.strip())

    # 创建一个文件夹来保存分类后的文件
    save_path = f'D:\\桌面\\animals\\{videoname}'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 将分类后的数据写入不同的文件
    for id, data_list in data_dict.items():
        with open(f'{save_path}\\{id}.txt', 'w') as file:
            for data_line in data_list:
                file.write(f"{data_line}\n")

# 调用函数，替换'r"D:\桌面\其他动物gt\video_1.txt"'为你的文件路径
classify_and_write_data(r"D:\桌面\video_out\video_10.txt", videoname='video_10', delimiter=',')
