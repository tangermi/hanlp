from pyhanlp import *


# 拼音转换
def Pinyin(document):
    # 原文
    print("\n原文: ",end = ' ')
    print(document)
    pinyin_list = HanLP.convertToPinyinList(document)
    # 数字音调
    print("\n数字音调: ",end = ' ')
    print(pinyin_list)
    # 符号音调
    print("\n符号音调: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getPinyinWithToneMark(), end=' ')
    # 无音调
    print("\n无音调: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getPinyinWithoutTone(), end=' ')
    # 声调
    print("\n声调: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getTone(), end=' ')
    # 声母
    print("\n声母: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getShengmu(), end=' ')
    # 韵母
    print("\n韵母: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getYunmu(), end=' ')
    # 输入法头
    print("\n输入法头: ",end = ' ')
    for pinyin in pinyin_list:
        print(pinyin.getHead(), end=' ')
        
#拼音转换
print('拼音转换' + '-' * 20)
Pinyin("拼音转换")