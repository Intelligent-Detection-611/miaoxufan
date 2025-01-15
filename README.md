# Project for Ecological Environment Data

# 脚本MAG_search_ImportantGeneID用来处理数据：输出目标文件夹下所有MAG的在各个重要途径下匹配的基因类型和个数

## 下载路径

MAG_search_ImportantGeneID.py 可以从以下路径下载 [MAG_search_ImportantGeneID.py](https://github.com/Intelligent-Detection-611/miaoxufan/blob/main/script/MAG_search_ImportantGeneID.py)

## 依赖环境
openpyxl  
panda  
os

## 操作步骤

    step1:将file_path 替换为存储重要和次要基因ID的xlsx文件路径
    step2:将total_MAG_path替换为存放所有MAG xlsx文件的文件夹路径
    step3:将output_path替换为存储输出结果的xlsx文件路径
    step4:运行脚本

# 脚本search.py：寻找所有文件夹下所需的MAG图片并输出相应的图片信息

### search.py 可以从以下路径下载 [search.py](https://github.com/Intelligent-Detection-611/miaoxufan/blob/main/script/search.py)

## 依赖环境
pip install os

## 操作步骤

    step1:将 /path/to/your/parent/folder 替换为你的父文件夹的实际路径。（将所有需要寻找的文件夹放在同一父文件夹下）
    step2:将 ["example.png", "image1.png", "image2.png"] 替换为你想要查找的图片名称列表。
    step3:将 image_search_results.txt 替换为你想要保存的 TXT 文件的路径和文件名。
    step4:运行脚本。

# 脚本compare.py：比较两个文件夹下的MAG图片并输出独有和共有的图片信息

### compare.py 可以从以下路径下载 [compare.py](https://github.com/Intelligent-Detection-611/miaoxufan/blob/main/script/compare.py)

## 依赖环境
pip install os

## 操作步骤

    step1:将 folder_A_path 后的文件路径替换为需要比较的第一个文件夹的路径
    step2:将 folder_B_path 后的文件路径替换为需要比较的第二个文件夹的路径
    step3:将 output_txt_path 后的文件路径替换为你想要保存的 TXT 文件的路径和文件名。
    step4:运行脚本。