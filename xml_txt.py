import argparse
import os
import re
from tqdm import tqdm

# # VOC格式的文件的存放路径
# path_voc = '../test/yolo/yolodata/Annotations/'
# # Yolo格式的标注文件目标路径
# path_yolo = '../test/yolo/yolodata/txt/'
# # 类名文件的路径
# path_class_name = '../test/yolo/yolodata/garbage.names'

def xml_txt(xml_path, txt_path, classnames_path):
    # 获取源文件夹下所有后缀为xml格式的文件
    re_xml = re.compile(r'.*(xml)')
    src_fname_list = [fname for fname in os.listdir(xml_path) if re_xml.match(fname)]
    if not src_fname_list:
        print("No XML files found in the provided directory.")
        return

    # 读取类名列表
    with open(classnames_path, encoding="utf-8") as f:
        class_name_list = f.read().split('\n')
        if not class_name_list:
            print("Classnames file is empty.")
            return

    # XML标签 正则表达式
    # 检索XML格式文件里面的关键信息
    cc = r'<xmin>(.*)</xmin>'
    xxmin = re.compile(r'<xmin>(.*)</xmin>')
    yymin = re.compile(r'<ymin>(.*)</ymin>')
    xxmax = re.compile(r'<xmax>(.*)</xmax>')
    yymax = re.compile(r'<ymax>(.*)</ymax>')
    wwidth = re.compile(r'<width>(.*)</width>')
    hheight = re.compile(r'<height>(.*)</height>')
    nname = re.compile(r'<name>(.*)</name>')

    # 遍历所有的XML文件
    for xml_fname in tqdm(src_fname_list, desc="Converting XML to TXT"):
        xml_file_path = os.path.join(xml_path, xml_fname)
        with open(xml_file_path, 'r', encoding="utf-8") as xml_file:
            xml_file_content = xml_file.read()

        name_list = re.findall(nname, xml_file_content)

        txt_fname = xml_fname.replace('.xml', '.txt')
        # print(f"{xml_fname} -> {txt_fname}")
        txt_file_path = os.path.join(txt_path, txt_fname)
        with open(txt_file_path, 'w', encoding="utf-8") as f:
            width = int(re.findall(wwidth, xml_file_content)[0])
            height = int(re.findall(hheight, xml_file_content)[0])

            for j in range(len(name_list)):
                name = name_list[j]
                class_id = class_name_list.index(name)
                xmin = int(re.findall(xxmin, xml_file_content)[j])
                ymin = int(re.findall(yymin, xml_file_content)[j])
                xmax = int(re.findall(xxmax, xml_file_content)[j])
                ymax = int(re.findall(yymax, xml_file_content)[j])

                if j != 0:
                    f.write('\n')
                f.write(
                    f"{class_id} {((xmin + xmax) / (2.0 * width)):.4f} {((ymin + ymax) / (2.0 * height)):.4f} "
                    f"{(float(xmax - xmin) / width):.4f} {(float(ymax - ymin) / height):.4f}")
    print("Conversion completed.")

if __name__ == "__main__":
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Convert VOC format to YOLO format")
    # 添加命令行参数
    parser.add_argument("--xml_path", type=str, help="Path to the XML format annotations directory")
    parser.add_argument("--txt_path", type=str, help="Path to the TXT format annotations directory")
    parser.add_argument("--classnames_path", type=str, help="Path to the class names file")
    # 解析命令行参数
    args = parser.parse_args()

    if args.voc_path and args.yolo_path and args.classnames_path:
        xml_txt(args.voc_path, args.yolo_path, args.classnames_path)