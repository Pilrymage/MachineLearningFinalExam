import pandas as pd
import os
def merge_csv():
    # 待处理的目录
    input_path = r'E:/360MoveData/Users/HM520/Desktop/weibo-crawler-master/总/'
    result_path = r'E:/360MoveData/Users/HM520/Desktop/weibo-crawler-master/总/'
    result_name= r'merged_result.csv'  # 合并后要保存的文件名
    # 进入工作目录
    os.chdir(input_path)
    # 获取该目录下所有文件的名字
    file_list = os.listdir()
    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(input_path + file_list[0], encoding="utf-8-sig")  # 编码默认UTF-8,根据需要需改
    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(result_path + result_name, encoding="utf-8-sig", index=False)
    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(file_list)):
        # 过滤隐藏文件
        if not file_list[i].startswith("."):
            try:
                # 根据文件名读取文件
                df = pd.read_csv(input_path + file_list[i], encoding="utf-8-sig")
                # index=True 在最左侧新增索引列；header=True  保留 表头
                df.to_csv(result_path + result_name, encoding="utf-8-sig", index=True, header=False, mode='a+')
            except:
                pass


merge_csv()