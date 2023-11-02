import argparse
from dataset import manual, auto
from de_weight import de_weight
from ren import ren
from xml_txt import xml_txt

# 创建命令行解析器
parser = argparse.ArgumentParser(description="Script to run various functions.")
# 添加支持的功能作为子命令
subparsers = parser.add_subparsers(dest="function")
ren_parser = subparsers.add_parser("ren")
ren_parser.add_argument("--source_path", type=str, help="Source folder path")
ren_parser.add_argument("--target_path", type=str, help="Target folder path")
de_weight_parser = subparsers.add_parser("de_weight")
de_weight_parser.add_argument("--image_path", type=str, help="Image directory path")
de_weight_parser.add_argument("--label_path", type=str, help="Label directory path")
voc_txt_parser = subparsers.add_parser("xml_txt")
voc_txt_parser.add_argument("--xml_path", type=str, help="Path to the XML format annotations directory")
voc_txt_parser.add_argument("--txt_path", type=str, help="Path to the TXY format annotations directory")
voc_txt_parser.add_argument("--classnames_path", type=str, help="Path to the class names file")
dataset_parser = subparsers.add_parser("dataset")
dataset_parser.add_argument("--file_path", type=str, help="Path to the original file directory")
dataset_parser.add_argument("--image_path", type=str, help="Path to the original image directory")
dataset_parser.add_argument("--label_path", type=str, help="Path to the original label directory")
dataset_parser.add_argument("--train_image_path", type=str, help="Path to the train image directory")
dataset_parser.add_argument("--train_label_path", type=str, help="Path to the train label directory")
dataset_parser.add_argument("--val_image_path", type=str, help="Path to the validation image directory")
dataset_parser.add_argument("--val_label_path", type=str, help="Path to the validation label directory")
dataset_parser.add_argument("--test_image_path", type=str, help="Path to the test image directory")
dataset_parser.add_argument("--test_label_path", type=str, help="Path to the test label directory")
dataset_parser.add_argument("--train", type=float, help="Percentage of data for training")
dataset_parser.add_argument("--val", type=float, help="Percentage of data for validation")
dataset_parser.add_argument("--test", type=float, help="Percentage of data for testing")
dataset_parser.add_argument("--mode", type=str, help="Choose mode (manual or auto)")
# 解析命令行参数
args = parser.parse_args()

# 在main.py中调用ren.py的ren函数
if args.function == "ren":
    ren(args.source_path, args.target_path)
# 在main.py中调用de_weight.py
elif args.function == "de_weight":
    de_weight(args.image_path, args.label_path)
# 在main.py中调用voc_txt.py
elif args.function == "xml_txt":
    xml_txt(args.xml_path, args.txt_path, args.classnames_path)
# 在main.py中调用dataset.py
elif args.function == "dataset":
    if args.mode == "manual":
        print("Running in manual mode")
        # 执行手动模式的功能
        manual(args.image_path, args.label_path, args.train_image_path, args.train_label_path, args.val_image_path,
               args.val_label_path, args.test_image_path, args.test_label_path, args.train, args.val, args.test)
    elif args.mode == "auto":
        print("Running in auto mode")
        # 执行自动模式的功能
        auto(args.train, args.val, args.test, args.image_path, args.label_path, args.file_path)
    else:
        print("Invalid mode. Use one of: manual, auto")
else:
    print("Invalid function. Use one of: de-weight, ren, xml_txt")
