import os

def find_images_in_subfolders(parent_folder, target_image_names, output_txt):
    with open(output_txt, 'w') as f:
        f.write(f'查找图片: {", ".join(target_image_names)}\n\n')

        for subdir_name in os.listdir(parent_folder):
            subdir_path = os.path.join(parent_folder, subdir_name)

            if os.path.isdir(subdir_path):
                f.write(f'文件夹: {subdir_name}\n')
                found_any = False  # 标记是否在该子文件夹中找到任何图片

                for target_image_name in target_image_names:
                    image_path = os.path.join(subdir_path, target_image_name)

                    if os.path.exists(image_path):
                        f.write(f'  找到图片: {target_image_name}\n')
                        f.write(f'  图片路径: {image_path}\n')
                        found_any = True
                    else:
                        f.write(f'  未找到图片: {target_image_name}\n')

                if not found_any:
                    f.write(f'  在该文件夹中未找到任何指定的图片\n')
                f.write('\n')

parent_folder_path = r"/path/to/your/parent/folder"  # 替换为你的父文件夹路径
images_to_find = ["example.png", "image1.png", "image2.png"]  # 替换为你想要查找的图片名称列表
output_txt_path = r"image_search_results.txt"  # 设置输出 TXT 文件的路径

find_images_in_subfolders(parent_folder_path, images_to_find, output_txt_path)

print(f"结果已保存到: {output_txt_path}")

