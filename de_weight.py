import argparse
import os
import subprocess
from tqdm import tqdm

# image_directory = '../test/dataset/images/train/'  # 图像文件夹路径
# label_directory = '../test/dataset/labels/train/'  # 标签文件夹路径
# 获取所有图像文件和标签文件的文件名
def de_weight(image_path, label_path):
    # 路径设置
    if not os.path.exists(image_path):
        print(f"Image directory '{image_path}' does not exist.")
        return
    if not os.path.exists(label_path):
        print(f"Label directory '{label_path}' does not exist.")
        return

    # 获取所有图像文件和标签文件的文件名
    image_files = os.listdir(image_path)
    label_files = os.listdir(label_path)

    # 获取只有文件名（不包含扩展名）的集合
    image_filenames = {os.path.splitext(filename)[0] for filename in image_files}
    label_filenames = {os.path.splitext(filename)[0] for filename in label_files}

    # 支持的图片和标签格式
    supported_image_formats = ['.jpg', '.jpeg', '.png', 'JPG']
    supported_label_formats = ['.txt', '.xml', '.json']

    # 查找没有标签文件的图像文件
    images_without_labels = image_filenames - label_filenames
    # 查找没有图像文件的标签文件
    labels_without_images = label_filenames - image_filenames

    # 删除没有标签文件的图像文件
    for image_filename in tqdm(images_without_labels, desc="Deleting images without labels"):
        for image_format in supported_image_formats:
            image_file_path = os.path.join(image_path, image_filename + image_format)
            if os.path.exists(image_file_path):
                os.remove(image_file_path)

        # 删除没有图像文件的标签文件
    for label_filename in tqdm(labels_without_images, desc="Deleting labels without images"):
        for label_format in supported_label_formats:
            label_file_path = os.path.join(label_path, label_filename + label_format)
            if os.path.exists(label_file_path):
                os.remove(label_file_path)

    print(f"Deleted {len(images_without_labels)} image files without corresponding label files.")
    print(f"Deleted {len(labels_without_images)} label files without corresponding image files.")


# 根据用户选择的功能调用相应的函数
if __name__ == "__main__":
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Script to run various functions.")
    # 添加命令行参数
    parser.add_argument("--image_path", type=str, help="Image directory path")
    parser.add_argument("--label_path", type=str, help="Label directory path")
    # 解析命令行参数
    args = parser.parse_args()

    if args.image_path and args.label_path:
        de_weight(args.image_path, args.label_path)