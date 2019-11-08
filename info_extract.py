from pyhanlp import *



class Info:

    # 关键词提取
    def key_words_extraction(self, sentence, n=5):
        print(HanLP.extractKeyword(sentence, n))

    # 自动摘要
    def summary(self, document, n=3):
        print(HanLP.extractSummary(document, n))

    # 短语提取
    def phrase_extraction(self, document, n=10):
        print(HanLP.extractPhrase(document, n))



if __name__ == '__main__':

    document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
            "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
            "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
            "严格地进行水资源论证和取水许可的批准。"
    
    info = Info()

    #关键词提取
    print('关键词提取' + '-' * 20)
    info.key_words_extraction(document,5)
    #自动摘要
    print('自动摘要' + '-' * 20)
    info.summary(document,3)
    #短语提取
    print('短语提取' + '-' * 20)
    info.phrase_extraction(document,3)
