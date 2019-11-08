from pyhanlp import *

class Suggest:
    # 文本推荐
    def Suggest(self, keywords, n, document):
        Suggester = JClass("com.hankcs.hanlp.suggest.Suggester")
        suggester = Suggester()
        for sentence in document:
            suggester.addSentence(sentence)
        for keyword in keywords:
            print(suggester.suggest(keyword,n))



if __name__ == '__main__':
    #文本推荐
    suggest = Suggest()

    print('文本推荐' + '-' * 20)
    keywords_for_suggest = ['发言','危机公共','mayun']
    document_for_suggest = ["威廉王子发表演说 呼吁保护野生动物\n" , "《时代》年度人物最终入围名单出炉 普京马云入选\n" , "日本保密法将正式生效 日媒指其损害国民知情权\n" ,"英报告说空气污染带来“公共健康危机”"]
    suggest.Suggest(keywords_for_suggest,1,document_for_suggest)