import os

def remove_images_without_labels(image_folder, label_extension='.txt'):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

    for image_file in image_files:
        # 获取图像文件的基本名（不带扩展名）
        image_name = os.path.splitext(image_file)[0]
        label_file = f"{image_name}{label_extension}"

        # 检查是否存在对应的标注文件
        if not os.path.exists(os.path.join(image_folder, label_file)):
            # 如果标注文件不存在，删除图片文件
            os.remove(os.path.join(image_folder, image_file))
            print(f"Deleted: {image_file}")

# 使用示例
image_folder = '/media/zhong/1.0T/20240809/20240823/img/8'  # 替换为你的图片和标注文件所在文件夹路径
remove_images_without_labels(image_folder)