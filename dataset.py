# 将图片和标注数据按比例切分为 训练集和测试集
import argparse
import shutil
import random
import os
from tqdm import tqdm

# # 数据集路径
# image_original_path = '../test/dataset/images/train/'
# label_original_path = '../test/dataset/labels/train/'
# # 训练集路径
# train_image_path = 'dataset_3/images/train/'
# train_label_path = 'dataset_3/labels/train/'
# # 验证集路径
# val_image_path = 'dataset_3/images/val/'
# val_label_path = 'dataset_3/labels/val/'
# # 测试集路径
# test_image_path = 'dataset_2/images/test/'
# test_label_path = 'dataset_2/labels/test/'

# # 数据集划分比例，训练集75%，验证集15%，测试集15%，按需修改
# train_percent = 0.8
# val_percent = 0.2
# test_percent = 0
# 检查文件夹是否存在
def mkdir(*paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")


def manual(image_path, label_path,
                  train_image_path, train_label_path,
                  val_image_path, val_label_path,
                  test_image_path, test_label_path,
                  train, val, test):
    mkdir(train_image_path, train_label_path, val_image_path, val_label_path, test_image_path, test_label_path)
    # 获取图像和标签文件列表
    image_files = os.listdir(image_path)
    label_files = os.listdir(label_path)

    # 随机打乱文件列表，但保持对应关系
    combined_files = list(zip(image_files, label_files))
    random.shuffle(combined_files)
    image_files, label_files = zip(*combined_files)

    # 划分数据集
    total_samples = len(image_files)
    num_train = int(total_samples * train)
    num_val = int(total_samples * val)
    num_test = total_samples - num_train - num_val

    # 复制文件到训练集、验证集和测试集
    for i in tqdm(range(num_train), desc="Copying to train"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(train_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(train_label_path, label_name))

    for i in tqdm(range(num_train, num_train + num_val), desc="Copying to val"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(val_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(val_label_path, label_name))

    for i in tqdm(range(num_train + num_val, total_samples), desc="Copying to test"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(test_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(test_label_path, label_name))

    print("Data splitting completed")

def auto(train, val, test, image_path, label_path, file_path):
    # 创建 file_path 目录（如果不存在）
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # 创建训练、验证和测试文件夹
    train_image_path = os.path.join(file_path, "train/images")
    train_label_path = os.path.join(file_path, "train/labels")
    val_image_path = os.path.join(file_path, "val/images")
    val_label_path = os.path.join(file_path, "val/labels")
    test_image_path = os.path.join(file_path, "test/images")
    test_label_path = os.path.join(file_path, "test/labels")

    # 创建文件夹
    os.makedirs(train_image_path)
    os.makedirs(train_label_path)
    os.makedirs(val_image_path)
    os.makedirs(val_label_path)
    os.makedirs(test_image_path)
    os.makedirs(test_label_path)

    # 获取图像和标签文件列表
    image_files = os.listdir(image_path)
    label_files = os.listdir(label_path)

    # 随机打乱文件列表，但保持对应关系
    combined_files = list(zip(image_files, label_files))
    random.shuffle(combined_files)
    image_files, label_files = zip(*combined_files)

    # 划分数据集
    total_samples = len(image_files)
    num_train = int(total_samples * train)
    num_val = int(total_samples * val)
    num_test = total_samples - num_train - num_val

    # 复制文件到训练集、验证集和测试集
    for i in tqdm(range(num_train), desc="Copying to train"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(train_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(train_label_path, label_name))

    for i in tqdm(range(num_train, num_train + num_val), desc="Copying to val"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(val_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(val_label_path, label_name))

    for i in tqdm(range(num_train + num_val, total_samples), desc="Copying to test"):
        image_name = image_files[i]
        label_name = label_files[i]
        shutil.copyfile(os.path.join(image_path, image_name), os.path.join(test_image_path, image_name))
        shutil.copyfile(os.path.join(label_path, label_name), os.path.join(test_label_path, label_name))

    print("Data splitting completed")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Split dataset into train, validation, and test sets")
    parser.add_argument("--file_path", type=str, help="Path to the original file directory")
    parser.add_argument("--image_path", type=str, help="Path to the original image directory")
    parser.add_argument("--label_path", type=str, help="Path to the original label directory")
    parser.add_argument("--train_image_path", type=str, help="Path to the train image directory")
    parser.add_argument("--train_label_path", type=str, help="Path to the train label directory")
    parser.add_argument("--val_image_path", type=str, help="Path to the validation image directory")
    parser.add_argument("--val_label_path", type=str, help="Path to the validation label directory")
    parser.add_argument("--test_image_path", type=str, help="Path to the test image directory")
    parser.add_argument("--test_label_path", type=str, help="Path to the test label directory")
    parser.add_argument("--train", type=float, help="Percentage of data for training")
    parser.add_argument("--val", type=float, help="Percentage of data for validation")
    parser.add_argument("--test", type=float, help="Percentage of data for testing")
    # 添加命令行参数
    parser.add_argument("--mode", type=str, help="Choose mode (manual or auto)")

    # 解析命令行参数
    args = parser.parse_args()

    if args.mode == "manual":
        print("Running in manual mode")
        manual(args.image_path, args.label_path, args.train_image_path, args.train_label_path, args.val_image_path,
               args.val_label_path, args.test_image_path, args.test_label_path, args.train, args.val, args.test)
    elif args.mode == "auto":
        print("Running in auto mode")
        # 执行自动模式的功能
        auto(args.train, args.val, args.test, args.image_path, args.label_path, args.file_path)
    else:
        print("Invalid mode. Use one of: manual, auto")


