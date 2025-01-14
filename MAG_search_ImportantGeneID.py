import pandas as pd
import os
import openpyxl

def read_excel_column_to_list(file_path, sheet_name, column_index=3):
    try:
        xls = pd.ExcelFile(file_path)
        if sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            if column_index < df.shape[1]: #Check if column_index is valid
                column_data = df.iloc[:, column_index].tolist()
                return column_data
            else:
                print(f"Error: Column at index {column_index} does not exist in sheet '{sheet_name}'.")
                return None
        else:
            print(f"Sheet '{sheet_name}' not found in the Excel file.")
            return None
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return None

def find_common_elements_comprehension(list1, list2):
    common_elements = [item for item in list1 if item in list2]
    return common_elements

def get_Important_ID(file_path, sheet_name_1, sheet_name_2):
    # 获取重要基因的KO_ID
    important_GeneID = read_excel_column_to_list(file_path, sheet_name_1, column_index=3)

    # 对工作表2进行特殊处理
    Secondary_Important_GeneID = read_excel_column_to_list(file_path, sheet_name_2, column_index=3)[1:]

    return important_GeneID, Secondary_Important_GeneID

def get_single_MAG_information(MAG_ID, MAG_path, MAG_sheet_name, important_GeneID, Secondary_Important_GeneID):
    #获得单个MAG的GeneID
    MAG_GeneID = read_excel_column_to_list(MAG_path, MAG_sheet_name, column_index=3)
    #获得相同的重要ID
    single_Important_ID = find_common_elements_comprehension(important_GeneID, MAG_GeneID)
    #获得相同的次重要ID
    single_Secondary_Important_ID = find_common_elements_comprehension(Secondary_Important_GeneID, MAG_GeneID)
    #分别获取重要ID和次重要ID的个数
    Important_ID_num = len(single_Important_ID)
    Secondary_Important_ID_num = len(single_Secondary_Important_ID)

    # 依次返回excel表需要存储的信息,MAG_ID,重要ID,次重要ID，重要ID个数,次重要ID个数
    return MAG_ID, single_Important_ID, single_Secondary_Important_ID, Important_ID_num, Secondary_Important_ID_num

def write_multiple_data_to_xlsx(all_data, output_path):
    # 创建一个新的工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 写入表头
    sheet.append(["MAG_ID", "Important IDs", "Secondary Important IDs", "Number of Important IDs", "Number of Secondary Important IDs"])

    # 写入数据
    for data in all_data:
        MAG_ID, single_Important_ID, Secondary_Important_ID, Important_ID_num, \
        Secondary_Important_ID_num = data
        sheet.append([str(MAG_ID), str(single_Important_ID), str(Secondary_Important_ID),
                      Important_ID_num, Secondary_Important_ID_num])

    # 保存文件
    workbook.save(output_path)
    print(f"Data has been written to {output_path}")

def write_all_information_to_xlsx(total_MAG_path, MAG_sheet_name, output_path):
    all_data_to_output = []  # 创建一个列表来存储所有数据
    for single_MAG_name in os.listdir(total_MAG_path):
        single_MAG_path = os.path.join(total_MAG_path, single_MAG_name)
        MAG_name = single_MAG_name.split('.')[0]
        data_to_output = get_single_MAG_information(MAG_name, single_MAG_path, MAG_sheet_name, important_GeneID, Secondary_Important_GeneID)
        all_data_to_output.append(data_to_output)  # 将数据添加到列表中

    write_multiple_data_to_xlsx(all_data_to_output, output_path)

if __name__ == '__main__':
    file_path = r'important Gene pathway' # Replace with your file path
    sheet_name_1 = '主路径'  # Replace with correct sheet name
    sheet_name_2 = '次要路径' # Replace with correct sheet name

    #获得重要和次重要基因的ID
    important_GeneID, Secondary_Important_GeneID = get_Important_ID(file_path, sheet_name_1, sheet_name_2)

    total_MAG_path = r'your all MAG pathway'
    MAG_sheet_name = "Sheet1"

    #存储最终结果的xlsx文件地址
    output_path = r'your excel file pathway'

    write_all_information_to_xlsx(total_MAG_path, MAG_sheet_name, output_path)



