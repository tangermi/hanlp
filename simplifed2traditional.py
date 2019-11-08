from pyhanlp import *

# 简繁转换
def TraditionalChinese2Simplified(sentence):
    print(HanLP.convertToSimplifiedChinese(sentence))

def simplified2Traditional(sentence):
    print(HanLP.convertToTraditionalChinese(sentence))


#简繁转换
print('简繁转换' + '-' * 20)
simplified2Traditional("用笔记本电脑写程序")
TraditionalChinese2Simplified('「以後等妳當上皇后，就能買士多啤梨慶祝了」')