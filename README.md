# DataFlowGen
使用说明书
    DataFlowGen是一个集成多种数据处理功能的使用工具，这个工具允许你执行不同的功能，包括重命名文件、去除重复数据、将XML格式的标注文件转换为TXT格式，以及创建数据集。
希望这个脚本可以帮助您处理大模型数据，提高你的工作效率，祝愿您在AI领域取得更大的成就！

（json转xml, json转txt, xml转json, txt转json, txt转xml功能还开发中，敬请期待。。。）

# 基本用法：
要使用这个脚本，你需要在命令行中指定一个子命令，然后提供相应的参数。以下是支持的子命令和它们的参数：

# 1. 重命名文件 (ren)

用法: 
```
python main.py ren --source_path SOURCE_PATH --target_path TARGET_PATH
```
参数说明：
```
--source_path: 源文件夹路径
--target_path: 目标文件夹路径
```
这个子命令会将指定源文件夹中的文件重命名并将它们移动到目标文件夹中，文件将会按照1、2、3 ...的格式重命名。
支持的格式：
```
['.jpg', '.jpeg', '.png', '.JPG']
```


# 2. 去除重复数据 (de_weight)
用法:
```
python main.py de_weight --image_path IMAGE_PATH --label_path LABEL_PATH
```
参数说明：
```
--image_path: 图像文件夹路径
--label_path: 标签文件夹路径
```
这个子命令会去除重复的图像和标签数据，以减小数据集的大小。

支持的格式：
```
# 支持的图片和标签格式
supported_image_formats = ['.jpg', '.jpeg', '.png', 'JPG']
supported_label_formats = ['.txt', '.xml', '.json']
```

# 3. 将XML标注文件转换为TXT格式 (xml_txt)
用法:
```
python main.py xml_txt --xml_path XML_PATH --txt_path TXT_PATH --classnames_path CLASSNAMES_PATH
```
参数说明：
```
--xml_path: XML格式标注文件夹路径
--txt_path: TXT格式标注文件夹路径
--classnames_path: 类别名称文件路径
```
这个子命令将XML格式的标注文件转换为TXT格式，并将类别名称保存到指定文件中。


# 4. 创建数据集 (dataset)
用法：
```
python main.py dataset --file_path FILE_PATH --image_path IMAGE_PATH --label_path LABEL_PATH --train_image_path TRAIN_IMAGE_PATH --train_label_path TRAIN_LABEL_PATH --val_image_path VAL_IMAGE_PATH --val_label_path VAL_LABEL_PATH --test_image_path TEST_IMAGE_PATH --test_label_path TEST_LABEL_PATH --train TRAIN --val VAL --test TEST --mode MODE
```
参数说明：
```
--file_path: 原始文件文件夹路径
--image_path: 原始图像文件夹路径
--label_path: 原始标签文件夹路径
--train_image_path: 训练图像文件夹路径
--train_label_path: 训练标签文件夹路径
--val_image_path: 验证图像文件夹路径
--val_label_path: 验证标签文件夹路径
--test_image_path: 测试图像文件夹路径
--test_label_path: 测试标签文件夹路径
--train: 训练数据占总数据的百分比
--val: 验证数据占总数据的百分比
--test: 测试数据占总数据的百分比
--mode: 模式选择，可以是 "manual" 或 "auto"这个子命令用于创建数据集，可以选择手动模式或自动模式，具体操作取决于选择的模式。
```
该脚本支持所有格式文件。

# 示例用法

以下是一些示例用法：
```
重命名文件:
python main.py ren --source_path source_directory --target_path target_directory

去除重复数据:
python main.py de_weight --image_path image_directory --label_path label_directory

将XML标注文件转换为TXT格式:
python main.py xml_txt --xml_path xml_directory --txt_path txt_directory --classnames_path classnames.txt

创建数据集 - 手动模式:
python main.py dataset --file_path file_directory --image_path image_directory --label_path label_directory --train_image_path train_image_directory --train_label_path train_label_directory --val_image_path val_image_directory --val_label_path val_label_directory --test_image_path test_image_directory --test_label_path test_label_directory --train 0.7 --val 0.2 --test 0.1 --mode manual

创建数据集 - 自动模式:
python main.py dataset --file_path file_directory --image_path image_directory --label_path label_directory --train 0.7 --val 0.2 --test 0.1 --mode auto
```
请根据你的需求选择适当的子命令和参数来运行脚本。
