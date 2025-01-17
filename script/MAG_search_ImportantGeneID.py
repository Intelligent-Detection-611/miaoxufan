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

def get_Important_ID(file_path, sheet_name):
    # 获取WL
    WL_GeneID = read_excel_column_to_list(file_path, sheet_name[0], column_index=3)

    # 获取H2
    H2_GeneID = read_excel_column_to_list(file_path, sheet_name[1], column_index=3)

    # 获取丙酮酸途径
    Pyruvate_GeneID = read_excel_column_to_list(file_path, sheet_name[2], column_index=3)

    # 获取乙酸途径
    Acetic_Acid_GeneID = read_excel_column_to_list(file_path, sheet_name[3], column_index=3)

    # 获取乙醇途径
    Ethanol_GeneID = read_excel_column_to_list(file_path, sheet_name[4], column_index=3)

    # 获取RBO
    RBO_GeneID = read_excel_column_to_list(file_path, sheet_name[5], column_index=3)

    # 获取重要基因的KO_ID
    Important_GeneID = read_excel_column_to_list(file_path, sheet_name[6], column_index=3)

    # 对工作表2进行特殊处理
    Secondary_GeneID = read_excel_column_to_list(file_path, sheet_name[7], column_index=3)[1:]

    return WL_GeneID, H2_GeneID, Pyruvate_GeneID, Acetic_Acid_GeneID, \
           Ethanol_GeneID, RBO_GeneID, Important_GeneID, Secondary_GeneID

def get_single_MAG_information(MAG_ID, MAG_path, MAG_sheet_name, WL_GeneID, H2_GeneID,
                                  Pyruvate_GeneID, Acetic_Acid_GeneID, Ethanol_GeneID,
                                  RBO_GeneID, Important_GeneID, Secondary_GeneID):
    # 获得单个MAG的GeneID
    MAG_GeneID = read_excel_column_to_list(MAG_path, MAG_sheet_name, column_index=3)
    # 获得WL路径ID
    single_WL_GeneID = find_common_elements_comprehension(WL_GeneID, MAG_GeneID)
    # 获得H2路径ID
    single_H2_GeneID = find_common_elements_comprehension(H2_GeneID, MAG_GeneID)
    # 获得Pyruvate路径ID
    single_Pyruvate_GeneID = find_common_elements_comprehension(Pyruvate_GeneID, MAG_GeneID)
    # 获得Acetic_Acid路径ID
    single_Acetic_Acid_GeneID = find_common_elements_comprehension(Acetic_Acid_GeneID, MAG_GeneID)
    # 获得Ethanol路径ID
    single_Ethanol_GeneID = find_common_elements_comprehension(Ethanol_GeneID, MAG_GeneID)
    # 获得RBO路径ID
    single_RBO_GeneID = find_common_elements_comprehension(RBO_GeneID, MAG_GeneID)
    # 获得主要路径ID
    single_Important_ID = find_common_elements_comprehension(Important_GeneID, MAG_GeneID)
    # 获得次要路径ID
    single_Secondary_ID = find_common_elements_comprehension(Secondary_GeneID, MAG_GeneID)
    # 获取各路径匹配的ID的个数

    WL_GeneID_num = len(single_WL_GeneID)
    H2_GeneID_num = len(single_H2_GeneID)
    Pyruvate_GeneID_num = len(single_Pyruvate_GeneID)
    Acetic_Acid_GeneID_num = len(single_Acetic_Acid_GeneID)
    Ethanol_GeneID_num = len(single_Ethanol_GeneID)
    RBO_GeneID_num = len(single_RBO_GeneID)
    Important_ID_num = len(single_Important_ID)
    Secondary_ID_num = len(single_Secondary_ID)

    # 依次返回excel表需要存储的信息,各途径匹配的ID和对应的ID个数
    return MAG_ID, single_WL_GeneID, single_H2_GeneID, single_Pyruvate_GeneID, single_Acetic_Acid_GeneID,\
           single_Ethanol_GeneID, single_RBO_GeneID, single_Important_ID, single_Secondary_ID, \
           WL_GeneID_num, H2_GeneID_num, Pyruvate_GeneID_num, Acetic_Acid_GeneID_num, \
           Ethanol_GeneID_num, RBO_GeneID_num, Important_ID_num, Secondary_ID_num

def write_multiple_data_to_xlsx(all_data, output_path):
    # 创建一个新的工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 写入表头
    sheet.append(["MAG_ID", "WL IDs", "H2 IDs", "Pyruvate IDs","Acetic_Acid IDs",
                  "Ethanol IDs", "RBO IDs", "Important IDs", "Secondary IDs",
                  "Number of WL IDs", "Number of H2 IDs", "Number of Pyruvate IDs",
                  "Number of Acetic_Acid IDs", "Number of Ethanol IDs", "Number of RBO IDs",
                  "Number of Important IDs", "Number of Secondary Important IDs"])

    # 写入数据
    for data in all_data:
        MAG_ID, single_WL_GeneID, single_H2_GeneID, single_Pyruvate_GeneID, single_Acetic_Acid_GeneID, \
        single_Ethanol_GeneID, single_RBO_GeneID, single_Important_ID, single_Secondary_ID, \
        WL_GeneID_num, H2_GeneID_num, Pyruvate_GeneID_num, Acetic_Acid_GeneID_num, \
        Ethanol_GeneID_num, RBO_GeneID_num, Important_ID_num, Secondary_ID_num = data
        sheet.append([str(MAG_ID), str(single_WL_GeneID), str(single_H2_GeneID), str(single_Pyruvate_GeneID),
                      str(single_Acetic_Acid_GeneID), str(single_Ethanol_GeneID), str(single_RBO_GeneID),
                      str(single_Important_ID), str(single_Secondary_ID),
                      WL_GeneID_num, H2_GeneID_num, Pyruvate_GeneID_num, Acetic_Acid_GeneID_num,
                      Ethanol_GeneID_num, RBO_GeneID_num,
                      Important_ID_num, Secondary_ID_num])

    # 保存文件
    workbook.save(output_path)
    print(f"Data has been written to {output_path}")

def write_all_information_to_xlsx(total_MAG_path, MAG_sheet_name, output_path, WL_GeneID, H2_GeneID,
                                  Pyruvate_GeneID, Acetic_Acid_GeneID, Ethanol_GeneID,
                                  RBO_GeneID, Important_GeneID, Secondary_GeneID):
    all_data_to_output = []  # 创建一个列表来存储所有数据
    for single_MAG_name in os.listdir(total_MAG_path):
        single_MAG_path = os.path.join(total_MAG_path, single_MAG_name)
        MAG_name = single_MAG_name.split('.')[0]
        data_to_output = get_single_MAG_information(MAG_name, single_MAG_path, MAG_sheet_name,
                                                    WL_GeneID, H2_GeneID,
                                  Pyruvate_GeneID, Acetic_Acid_GeneID, Ethanol_GeneID,
                                  RBO_GeneID, Important_GeneID, Secondary_GeneID)
        all_data_to_output.append(data_to_output)  # 将数据添加到列表中

    write_multiple_data_to_xlsx(all_data_to_output, output_path)

if __name__ == '__main__':
    file_path = r'important Gene pathway' # Replace with your file path
    sheet_name_1 = 'WL'
    sheet_name_2 = 'H2'
    sheet_name_3 = 'Pyruvate'#丙酮酸途径
    sheet_name_4 = 'Acetic_Acid'#乙酸途径
    sheet_name_5 = 'Ethanol'#乙醇途径
    sheet_name_6 = 'RBO'
    sheet_name_7 = 'Important'  # 主路径
    sheet_name_8 = 'Secondary' # 次要路径
    sheet_name = ['WL', 'H2', 'Pyruvate', 'Acetic_Acid', 'Ethanol', 'RBO', 'Important', 'Secondary']

    #获得重要和次重要基因的ID
    WL_GeneID, H2_GeneID, Pyruvate_GeneID, Acetic_Acid_GeneID, \
    Ethanol_GeneID, RBO_GeneID, Important_GeneID, Secondary_GeneID = \
        get_Important_ID(file_path, sheet_name)

    total_MAG_path = r'your all MAG pathway'
    MAG_sheet_name = "Sheet1"

    #存储最终结果的xlsx文件地址
    output_path = r'your excel file pathway'
    write_all_information_to_xlsx(total_MAG_path, MAG_sheet_name, output_path, WL_GeneID, H2_GeneID,
                                  Pyruvate_GeneID, Acetic_Acid_GeneID, Ethanol_GeneID,
                                  RBO_GeneID, Important_GeneID, Secondary_GeneID)



