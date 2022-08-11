# README

## 环境安装

1. 安装[python](https://www.python.org/downloads/) (P.S. 注意安装过程中，一定要将python加入到系统环境变量中)[安装指南](https://zhuanlan.zhihu.com/p/104502997)
2. 执行以下命令

```PowerShell
pip install pandas -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

## 使用说明

1. 存放位置
   - pvc文件
     - `data -> <电机型号> -> "01 PVC数据" -> "<电机型号> M[1..].pvc"`
   - 电流文件
     - `data -> <电机型号> -> "02 电流数据" -> "<电机型号> M[1..].pvc"`

## 运行命令

1. 获取电流数据
   - 在PowerShell中转移到 `模型采集` 目录
     ```PowerShell
     python .\programs\current_data.py <电机型号> <模型数量>
     ```
2. 获取PVC总电流数据
   - 在PowerShell中转移到 `模型采集` 目录
     ```PowerShell
     python .\programs\pvc_data.py <电机型号> <模型数量>
     ```
3. 获取PVC正电流数据
  - 在PowerShell中转移到 `模型采集` 目录
     ```PowerShell
     python .\programs\pvc_data_positive.py <电机型号> <模型数量>
     ```
4. 获取PVC负电流数据
   在PowerShell中转移到 `模型采集` 目录
     ```PowerShell
     python .\programs\pvc_data_negative.py <电机型号> <模型数量>
     ```