#!/usr/bin/python3

import pandas as pd
from sys import argv


def GetData(_model_tag, _model_num):
    # Open file
    file_path = "..\\模型采集\\data\\" + _model_tag + "\\02 电流参数\\" + _model_tag + " M" + str(_model_num) + ".csv"
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
    return output_list


if __name__ == '__main__':
    # Check if the number of arguments is correct
    args = len(argv)
    if args < 2:
        print("Usage: python current_data.py <模型型号> <电机数量>")
        exit(1)
    
    # Get parameters
    model_tag = argv[1]
    model_num = int(argv[2])

    # Initialize the list
    data_dict = dict()
    index = list(range(600))

    # Read data
    print("===Start to get data===")
    for i in range(model_num):
        data_dict["M" + str(i + 1)] = GetData(model_tag, i + 1)
    print("Finish getting data===\n")
    
    # Write data
    print("===Start to write csv file===")
    file_path = "..\\模型采集\\data\\" + model_tag + "\\02 电流参数\\" + model_tag + " 总电流参数.csv"
    df = pd.DataFrame(data_dict, index=index)   
    df.to_csv(file_path)
    print("===Finished writing csv file===")
