import os
# 读取原始txt文件
with open(r'D:\桌面\蜂猴论文\刻板行为\data_make\moving_know\video_1.txt', "r") as file:
    content = file.read()

# 提取列表内容
list_content = [eval(line.strip()) for line in content.strip().split("\n")]

# Grouping the sublists based on the 5th element
grouped_content = {}
max=0
for sublist in list_content:
    for line in sublist:
        key=line[4]
        if key not in grouped_content:
            grouped_content[key]=[]
        grouped_content[key].append(line)

# 输出文件夹路径
output_directory = "./vid_1/"

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 写入不同的txt文件，每个文件包含一个key值的列表
created_files_paths = []  # 用于存储创建的文件路径
for key, sublists in grouped_content.items():
    output_file_path = f"{output_directory}group_{key}.txt"
    with open(output_file_path, "w") as file:
        for sublist in sublists:
            line = " ".join(map(str, sublist))
            file.write(line + "\n")
    created_files_paths.append(output_file_path)

print(created_files_paths)  # 返回创建的文件路径列表


