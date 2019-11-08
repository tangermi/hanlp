from pyhanlp import *
import zipfile
import os

from pyhanlp.static import download, remove_file, HANLP_DATA_PATH

class HanlpWord2Vec:
    def test_data_path(self):
        """
        获取测试数据路径，位于$root/data/test，根目录由配置文件指定。
        :return:
        """
        data_path = os.path.join(HANLP_DATA_PATH, 'test')
        if not os.path.isdir(data_path):
            os.mkdir(data_path)
        return data_path

    def ensure_data(self, data_name, data_url):
        root_path = self.test_data_path()
        dest_path = os.path.join(root_path, data_name)
        if os.path.exists(dest_path):
            return dest_path
        if data_url.endswith('.zip'):
            dest_path += '.zip'
        download(data_url, dest_path)
        if data_url.endswith('.zip'):
            with zipfile.ZipFile(dest_path, "r") as archive:
                archive.extractall(root_path)
            remove_file(dest_path)
            dest_path = dest_path[:-len('.zip')]
        return dest_path


    # 语义距离
    def Document_similarity(self, document1, document2):
        CoreSynonymDictionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")
        print(f"“{document1}”与“{document2}”之间的距离与相似度:")
        print(CoreSynonymDictionary.distance(document1, document2), CoreSynonymDictionary.similarity(document1, document2))
        

    def Nearest_word(self, keywords):
        WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')
        model_path = os.path.join(self.ensure_data('hanlp-wiki-vec-zh', 'http://file.hankcs.com/model/hanlp-wiki-vec-zh.zip'),
            'hanlp-wiki-vec-zh.txt')
        word2vec = WordVectorModel(model_path)
        for keyword in keywords:
            print(f"“{keyword}”的相似词语：")
            print(word2vec.nearest(keyword))

    def Nearest_document(self, keywords, document):
        WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')
        DocVectorModel = JClass("com.hankcs.hanlp.mining.word2vec.DocVectorModel")
        model_path = os.path.join(self.ensure_data('hanlp-wiki-vec-zh', 'http://file.hankcs.com/model/hanlp-wiki-vec-zh.zip'),
            'hanlp-wiki-vec-zh.txt')
        word2vec = WordVectorModel(model_path)
        doc2vec = DocVectorModel(word2vec)

        for i, sentence in enumerate(document):
            doc2vec.addDocument(i, sentence)
        for keyword in keywords:
            print(f"\n“{keyword}”的相关文档：")
            for res in doc2vec.nearest(keyword):
                print('%s = %.2f' % (docs[res.getKey().intValue()], res.getValue().floatValue()))

if __name__ == '__main__':

    keywords_for_nearest_document = ['体育', '农业', '我要看比赛', '要不做饭吧']
    docs = ["山东苹果丰收", "农民在江苏种水稻", "奥运会女排夺冠", "世界锦标赛胜出", "中国足球失败"]

    word2vec = HanlpWord2Vec()

    word2vec.Document_similarity(keywords_for_nearest_document[0],keywords_for_nearest_document[2])
    word2vec.Document_similarity(keywords_for_nearest_document[0],keywords_for_nearest_document[1])
    print('-'*20)
    word2vec.Nearest_word(keywords_for_nearest_document)
    print('-'*20)
    word2vec.Nearest_document(keywords_for_nearest_document,docs)   
