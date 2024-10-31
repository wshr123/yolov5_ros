import os
import shutil
import random

# 设置随机种子以确保可重复性
random.seed(42)

# 定义源数据集路径
source_dir = '/home/zhong/Desktop/fake_crop/img_label'  # 替换为你实际的数据集文件夹路径
# 定义目标训练集和验证集路径
train_dir = '/home/zhong/Desktop/fake_crop/train'  # 替换为你实际的训练集文件夹路径
val_dir = '/home/zhong/Desktop/fake_crop/val'  # 替换为你实际的验证集文件夹路径

# 创建目标文件夹（如果不存在）
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# 定义训练集与验证集的划分比例
train_ratio = 0.7  # 80%用作训练集，20%用作验证集

# 获取所有图片文件
image_files = [f for f in os.listdir(source_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

# 打乱图片文件列表顺序
random.shuffle(image_files)

# 计算训练集的文件数
train_size = int(len(image_files) * train_ratio)

# 划分训练集和验证集
train_files = image_files[:train_size]
val_files = image_files[train_size:]


# 函数：移动文件
def move_files(file_list, target_dir):
    for file_name in file_list:
        # 移动图片文件
        image_path = os.path.join(source_dir, file_name)
        shutil.move(image_path, target_dir)

        # 移动对应的txt文件
        txt_file = os.path.splitext(file_name)[0] + '.txt'
        txt_path = os.path.join(source_dir, txt_file)
        if os.path.exists(txt_path):
            shutil.move(txt_path, target_dir)
        else:
            print(f"Warning: {txt_file} not found for {file_name}")


# 将文件移动到训练集和验证集文件夹
move_files(train_files, train_dir)
move_files(val_files, val_dir)

print(f"Training files moved to: {train_dir}")
print(f"Validation files moved to: {val_dir}")
