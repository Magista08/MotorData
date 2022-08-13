#!/usr/bin/python3

import pandas as pd
import os
from sys import argv


def GetData(_model_tag, _model_version, _model_num):
    # Open file
    pre_file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = pre_file_path + "\\..\\模组数据\\" + _model_tag + "\\" +  _model_tag + " " + _model_version + \
                "\\02 电流参数\\" + "M" + str(_model_num) + ".csv"
    try:
        open_signal = open(file_path)
        open_signal.close()
    except FileNotFoundError:
        print(file_path + " is not found.")
        exit(1)
    except PermissionError:
        print("You don't have permission to access this file: " + file_path )
    pFile = open(file_path, "r")

    # Basic parameters
    output_list = list()

    # Read file line by line
    for i in pFile:
        # Split the line
        data_list = i.split(",")
        
        # Get rid of the redundant line
        if (len(data_list) != 8) or (data_list[0][0].isdigit() == False):
            continue
        
        # Get the current data
        current = float(data_list[7][:-1])
        output_list.append(current)
    
    # return 
    pFile.close()
    output_list.append(max(output_list))
    output_list.append(min(output_list))
    return output_list


if __name__ == '__main__':
    # Check if the number of arguments is correct
    args = len(argv)
    if args < 3:
        print("USAGE: python current_data.py <模型型号> <版本号> <电机数量>")
        exit(1)
    
    # Get parameters
    model_tag = argv[1]
    model_version = argv[2]
    model_num = int(argv[3])

    # Initialize the list
    data_dict = dict()
    index = list(range(600))
    index.append("Max current")
    index.append("Min current")

    # Read data
    print("===开始获取数据===")
    for i in range(model_num):
        data_dict["M" + str(i + 1)] = GetData(model_tag, model_version, i + 1)
    print("===提取数据完成===\n")
    
    # Write data
    print("===开始写入csv文件===")
    pre_file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = pre_file_path + "\\..\\模组数据\\" + model_tag + "\\" + model_tag + " " + model_version + "\\" + model_tag + " 实时电流参数.csv"
    df = pd.DataFrame(data_dict, index=index)   
    df.to_csv(file_path)
    print("===文件写入完成===")
