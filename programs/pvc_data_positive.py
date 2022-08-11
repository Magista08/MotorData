#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pandas as pd
from sys import argv


def GetIndex(_model_tag, _model_version):
    # Get max and min position from the first file
    first_file_path = "模组数据\\" + _model_tag + "\\" +  _model_tag + " " + _model_version + \
                      "\\01 PVC参数\\M1.pvc"
    try:
        open_signal = open(first_file_path)
        open_signal.close()
    except FileNotFoundError:
        print(first_file_path + " is not found.")
        exit(1)
    except PermissionError:
        print("You don't have permission to access this file: " + first_file_path )
        exit(-1)
    pFirstFile = open(first_file_path, "r")

    # INIT basic parameters
    nMaxNum = 0
    nMinNum = 0
    column_index = list()

    # Update the min and max
    for j in pFirstFile:
        tag = j.split("=")
        if tag[0] == "MaxPos ":
            nMaxNum = int(tag[1][:-1])
        elif tag[0] == "MinPos ":
            nMinNum = int(tag[1][:-1])
        elif (nMaxNum != 0) and (nMinNum != 0):
            break
    pFirstFile.close()

    # Print the average
    for dividend in range(8):
        num = float(abs(nMinNum) + abs(nMaxNum)) / 8
        num = num * dividend + nMinNum
        for n in range(8):
            column_index.append(num)

    # Write data
    column_index.append("Max current")
    column_index.append("Min current")
    return column_index


def GetData(_model_tag, _model_version,  _model_num):
    # Open file
    file_path = "模组数据\\" + _model_tag + "\\" +  _model_tag + " " + _model_version + \
                "\\01 PVC参数\\M" + str(_model_num) + ".pvc"
    try:
        open_signal = open(file_path)
        open_signal.close()
    except FileNotFoundError:
        print(file_path + " is not found.")
        exit(1)
    except PermissionError:
        print("You don't have permission to access this file: " + file_path )
    pFile = open(file_path, "r")
    
    # Read file line by line
    column_1 = list()
    for i in pFile:
        tag = i.split("=")
        data = i.split(",")

        # Get rid of the useless data
        if (len(tag) > 1) and (len(data) == 1):
            continue
        
        # Get the positive current and the negative current
        column_1.append(float(data[-2]))

    pFile.close()

    # Process the data
    column_1.append(max(column_1))
    column_1.append(min(column_1))
    return column_1


if __name__ == '__main__':
    # Check if the number of arguments is correct
    args = len(argv)
    if args < 4:
        print("USAGE: python pvc_data.py <模型型号> <版本号> <电机数量>")
        exit(1)

    # Get parameters
    model_tag = argv[1]
    model_version = argv[2]
    model_num = int(argv[3])

    # Initialize the list
    output_dict = dict()
    print("===计算位置检索===")
    index_list = GetIndex(model_tag, model_version)
    print("===位置检索计算完成===" + "\n")

    # Get Data
    print("===开始获取数据===")
    for i in range(model_num):
        model_num_column_1 = GetData(model_tag, model_version,  i + 1)
        output_dict["M" + str(i + 1) +"(mA)"] = model_num_column_1
    print("===数据获取完成===" + "\n")

    # to csv file
    print("===开始写入csv文件===")
    file_path = "模组数据\\" + model_tag + "\\" + model_tag + " " + model_version + \
                      "\\" + model_tag + " PVC正向电流参数.csv"
    df = pd.DataFrame(output_dict, index=index_list)   
    df.to_csv(file_path)
    print("===csv文件写入完成===")
