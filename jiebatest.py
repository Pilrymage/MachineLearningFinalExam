# encoding=utf-8
import jieba
import re
jieba.load_userdict("train/word.txt")
line='#中国的传统服饰有多美# “中国有礼仪之大，故称夏，有服章之美，谓之华。”服饰是中华文明的外展。CCTV-1除夕下午档春节特别节目#古韵新春#，我在@央视一套 ，与您一起，品味东方美学。'
# s=line
# p = re.compile(r'http?://.+$')  # 正则表达式，提取URL
# result = p.findall(line)  # 找出所有url
# if len(result):
#     for i in result:
#         s = s.replace(i, '')  # 一个一个的删除
# seg_list = jieba.cut(str（s).replace(' ', ''))  # 默认是精确模式
stop = [line.strip() for line in open('ad/stop.txt', 'r', encoding='utf-8').readlines()]  # 停用词
print(list(set(jieba.cut(line)) - set(stop)))
print(list(jieba.cut(line)))