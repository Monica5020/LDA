import data_deal as dd
from gensim import corpora ,models
import gensim

# 读取text文件
def read_text_file(url):
    text=open(url,'r',encoding= 'utf-8')
    return text.read().split('\n')

# 文本处理
def deal_words(contents):
    contents =dd.remove_blank_space(contents )
    contents =dd.cut_words(contents)
    contents=dd.drop_stopwords(contents)
    # contents=dd.pos_contents(contents)
    return contents

# lda模型
def lda_model(train_data):
    # 读取预测分类数据
    test_data=deal_words(read_text_file('data/test_data.txt'))
    # 拼接提取词典库
    contents=train_data +test_data
    # 根据文本获取词典
    dictionary=corpora.Dictionary(contents )
    # 根据词典创建语料库
    corpus=[dictionary.doc2bow(doc) for doc in train_data  ]
    lda=gensim.models.ldamodel.LdaModel(corpus,num_topics= 13,id2word= dictionary,passes= 5)

    data=lda.print_topics(num_topics= 13,num_words= 3)
    for item in data:
        print(item)
        # print('--------------------split line---------------------')
    # lda.save('model/safe_LDA.model')
    # 测试主题分类
    test_vec=[dictionary.doc2bow(doc) for doc in test_data  ]
    target={}
    for i,item in enumerate (test_vec ):
        topic=lda.get_document_topics(item)
        keys=target.keys()
        print('第',i+1,'条记录分类结果：',topic )
if __name__ =='__main__':
    contents=read_text_file('data/train_data.txt')
    contents=deal_words(contents )
    # print('进行训练的语料：')
    # print(contents)
    lda_model(contents)