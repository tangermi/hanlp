# -*- coding:utf-8 -*-
from pyhanlp import *
import time

"""
HanLP
分词，词性，关键词，摘要，句法分析
"""
class HanlpSegment:
    def __init__(self):
        print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))

    def cut(self, sentence):
        print(HanLP.segment(sentence))
        for term in HanLP.segment(sentence):
            print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性

    # 标准分词
    def stantardTokenize(self, sentence):
        StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
        print(StandardTokenizer.segment(sentence))

    # NLP分词
    def NLPTokenize(self, sentence):
        NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
        print(NLPTokenizer.segment(sentence))

    # 索引分词
    def IndexTokenize(self, sentence):
        IndexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
        IndexTokenizer.segment(sentence)

    # N-最短路径分词
    def NShortSegment(self, sentences):
        nShortSegment = JClass("com.hankcs.hanlp.seg.NShort.NShortSegment")
        DijkstraSegment = JClass("com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment")

        nshort_segment = nShortSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
        shortest_segment = DijkstraSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
        
        for sentence in sentences:
            print("N-最短分词：{}  最短路分词：{}".format(nshort_segment.seg(sentence), shortest_segment.seg(sentence)))
    
    # CRF分词
    def CRFAnalyze(self, document):
        CRFLexicalAnalyzer = JClass("com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer")
        analyzer = CRFLexicalAnalyzer()
        for sentence in document:
            print(analyzer.analyze(sentence))

    # 极速词典分词
    def HighSpeedSegment(self, sentence):
        SpeedTokenizer = JClass("com.hankcs.hanlp.tokenizer.SpeedTokenizer")
        start = time.time()
        pressure = 1000000
        for i in range(pressure):
            SpeedTokenizer.segment(sentence)
        cost_time = time.time()-start
        print("SpeedTokenizer分词速度：%.2f字每秒" % (len(sentence) * pressure / cost_time))

    # 用户自定义词典
    def CustomisedDict(self, sentence):
        CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
        CustomDictionary.add("攻城狮")  # 动态增加
        CustomDictionary.insert("白富美", "nz 1024")  # 强行插入
        # CustomDictionary.remove("攻城狮");  # 删除词语（注释掉试试）
        CustomDictionary.add("单身狗", "nz 1024 n 1")
        # print(CustomDictionary.get("单身狗"))

        print(HanLP.segment(sentence))

    # 中国人名识别
    def Segment_with_chinese_name(self, sentence):
        segment = HanLP.newSegment().enableNameRecognize(True)
        print(segment.seg(sentence))

    # 音译人名识别
    def Segment_with_translated_name(self, sentence):
        segment = HanLP.newSegment().enableTranslatedNameRecognize(True)
        print(segment.seg(sentence))

    # 日本人名识别
    def Segment_with_jp_name(self, sentence):
        segment = HanLP.newSegment().enableJapaneseNameRecognize(True)
        print(segment.seg(sentence))

    # 地名识别
    def Segment_with_place_name(self, sentence):
        segment = HanLP.newSegment().enablePlaceRecognize(True)
        print(segment.seg(sentence))

    # 机构名识别
    def Segment_with_org_name(self, sentence):
        segment = HanLP.newSegment().enableOrganizationRecognize(True)
        print(segment.seg(sentence))



if __name__ == '__main__':
    hanlp = HanlpSegment()
    testCases = [
        "商品和服务",
        "结婚的和尚未结婚的确实在干扰分词啊",
        "买水果然后来世博园最后去世博会",
        "中国的首都是北京",
        "欢迎新老师生前来就餐",
        "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
        "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
    document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
               "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
               "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
               "严格地进行水资源论证和取水许可的批准。"
    # # 分词
    # for sentence in testCases:
    #     hanlp.cut(sentence)
    #
    # # 标准分词
    # print('标准分词' + '-' * 20)
    # for sentence in testCases:
    #     hanlp.stantardTokenize(sentence)
    #
    # # NLP分词
    # print('NLP分词' + '-' * 20)
    # for sentence in testCases:
    #     hanlp.NLPTokenize(sentence)
    #
    # # 索引分词
    # print('索引分词' + '-' * 20)
    # for sentence in testCases:
    #     hanlp.IndexTokenize(sentence)
    #
    # # N-最短路径分词
    # print('N-最短路径分词' + '-' * 20)
    # for sentence in testCases:
    #     hanlp.NShortSegment(sentence)
    #
    # # 极速词典分词
    # print('极速词典分词' + '-' * 20)
    # # for sentence in testCases:
    # #     hanlp.HighSpeedSegment(sentence)
    #
    # # CRF分词
    # print('CRF分词' + '-' * 20)
    # hanlp.CRFAnalyze(testCases)
    # # 用户自定义词典
    # print('用户自定义词典' + '-' * 20)
    # sentence_for_customisedDict = "攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰"
    # hanlp.CustomisedDict(sentence_for_customisedDict)
    # # 中国人名识别
    # sentence_for_chinese_name = "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。"
    # print('中国人名识别' + '-' * 20)
    # hanlp.Segment_with_chinese_name(sentence_for_chinese_name)
    # # 音译人名识别
    # sentence_for_translated_name = "一桶冰水当头倒下，微软的比尔盖茨、Facebook的扎克伯格跟桑德博格、亚马逊的贝索斯、苹果的库克全都不惜湿身入镜，这些硅谷的科技人，飞蛾扑火似地牺牲演出，其实全为了慈善。"
    # print('音译人名识别' + '-' * 20)
    # hanlp.Segment_with_translated_name(sentence_for_translated_name)
    # # 日本人名识别
    # sentence_for_jp_name = "北川景子参演了林诣彬导演的《速度与激情3》"
    # print('日本人名识别' + '-' * 20)
    # hanlp.Segment_with_jp_name(sentence_for_jp_name)
    # 地名识别
    sentence_for_place_name = "蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机"
    print('地名识别' + '-' * 20)
    hanlp.Segment_with_place_name(sentence_for_place_name)
    # # 机构名识别
    # sentence_for_org_name = "我在上海林原科技有限公司兼职工作，偶尔去地中海影城看电影。"
    # print('机构名识别' + '-' * 20)
    # hanlp.Segment_with_org_name(sentence_for_org_name)




