import os

def find_common_elements_comprehension(list1, list2):
    common_elements = [item for item in list1 if item in list2]
    return common_elements

def find_different_elements_comprehension(list1, list2):
    #如果list1中的某个元素不存在于list2中，则将该元素添加到新列表中。
    different_elements = [item for item in list1 if item not in list2]
    return different_elements

def compare_folders(folder_A, folder_B, output_txt):
    folder_A_name = folder_A.split('\\')[-1]
    folder_B_name = folder_B.split('\\')[-1]
    folder_name = [folder_A_name] + [folder_B_name]

    with open(output_txt, 'w') as f:
        f.write(f'比较的两个文件夹: {",   ".join(folder_name)}\n\n')

        folder_a = [subdir_name for subdir_name in os.listdir(folder_A) if subdir_name.endswith('.png')]

        folder_b = [subdir_name for subdir_name in os.listdir(folder_B) if subdir_name.endswith('.png')]

        common_pic = find_common_elements_comprehension(folder_a, folder_b)
        common_num = len(common_pic)
        different_a = find_different_elements_comprehension(folder_a, common_pic)
        # folder_a中有,common_pic中没有，也就是folder_a中与folder_b中不同的元素部分
        num_different_a = len(different_a)
        different_b = find_different_elements_comprehension(folder_b, common_pic)
        num_different_b = len(different_b)

        if common_pic:#存在相同文件A

            f.write(f'共有图片 {common_num}张 ：  {common_pic}\n\n')
        else:
            f.write(f'不存在相同图片: \n\n')

        if different_a:#A文件夹中存在不同的文件
            f.write(f'文件夹: {folder_A_name} 中独有的图片有 {num_different_a}张 ： {different_a} \n\n')
        else:
            f.write(f'文件夹: {folder_A_name} 中不存在独有的图片 \n\n')

        if different_b:#A文件夹中存在不同的文件
            f.write(f'文件夹: {folder_B_name} 中独有的图片有 {num_different_b}张 ： {different_b} \n\n')
        else:
            f.write(f'文件夹: {folder_B_name} 中不存在独有的图片 \n\n')

folder_A_path = r"your first folder pathway"
folder_B_path = r"your second folder pathway"

output_txt_path = r"your txt result pathway"  # 设置输出 TXT 文件的路径

compare_folders(folder_A_path, folder_B_path, output_txt_path)

# print(f"结果已保存到: {output_txt_path}")


