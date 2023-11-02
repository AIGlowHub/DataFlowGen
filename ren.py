import argparse
import os
import shutil
from tqdm import tqdm

# 支持的图像格式
supported_image_formats = ['.jpg', '.jpeg', '.png', '.JPG']

# 定义ren函数
def ren(source_path, target_path):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"Target folder '{target_path}' created.")

    # 获取源文件夹中的所有图像文件
    image_files = [f for f in os.listdir(source_path) if
                   any(f.lower().endswith(ext) for ext in supported_image_formats)]

    # 排序图像文件
    image_files.sort()

    # 使用tqdm创建进度条
    for i, image_file in tqdm(enumerate(image_files), total=len(image_files), desc="rename..."):
        source_file = os.path.join(source_path, image_file)
        target_filename = f'{i+1}.jpg'  # 创建格式化的文件名，例如0001.jpg
        target_file = os.path.join(target_path, target_filename)

        # 重命名并移动文件
        shutil.copy(source_file, target_file)

    print("Image renaming and moving completed")

# 如果想要在命令行下运行ren.py脚本时执行此函数，可以添加如下代码
if __name__ == "__main__":
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Script to rename and move image files.")
    # 添加命令行参数
    parser.add_argument("--source_path", type=str, help="Source folder path")
    parser.add_argument("--target_path", type=str, help="Target folder path")
    # 解析命令行参数
    args = parser.parse_args()

    if args.source_path and args.target_path:
        ren(args.source_path, args.target_path)