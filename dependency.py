from pyhanlp import *

# 依存句法分析
def DependencyParser(sentence):
    print(HanLP.parseDependency(sentence))

testCases = [
    "商品和服务",
    "结婚的和尚未结婚的确实在干扰分词啊",
    "买水果然后来世博园最后去世博会",
    "中国的首都是北京",
    "欢迎新老师生前来就餐",
    "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
    "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]


# 依存句法分析
print('依存句法分析' + '-' * 20)
for sentence in testCases:
    DependencyParser(sentence)
