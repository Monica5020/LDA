# coding=utf-8
import jieba
import jieba.posseg as pos
import pandas as pd
jieba.load_userdict("data/dictionary")

# 去除文本空格
# input:['文本1','文本2',...'文本n']
# output:['去除空格后的文本1','去除空格后的文本2',...,'去除空格后的文本n']
def remove_blank_space(contents):
    contents_new=map(lambda s : s.replace(' ',''),contents)
    contents_new = map(lambda s: s.replace('\n', ''), contents_new )
    return list(contents_new)

# 分词，引入外部词典
def cut_words(contents):
    cut_contents=map(lambda s: list(jieba .lcut(s)),contents )
    return list(cut_contents)

# 去除停用词
def drop_stopwords(contents):
    stopwords_file=open('data/stopwords.txt','r',encoding= 'gbk')
    stopwords=stopwords_file.read().split('\n')
    # 定义去除停用词后要返回的结果
    contents_new=[]
    for line in contents :
        line_clean=[]
        for word in line :
            if word in stopwords :
                continue
            else:
                line_clean.append(word )
        contents_new.append(line_clean )
    return contents_new

# 词性标注后保留动词和名词
def pos_contents(contents):
    contents_new=[]
    for content in contents :
        line_clean=[]
        words=pos.cut(content[0] )
        for w in words:
            if w.flag in ['v','n','x']:
                line_clean.append(w.word)
            else:
                continue
        contents_new .append(line_clean )
    return contents_new



# 计算IDF
def deal_contents(contents):
    # 定义记录IDF的数据
    word_counts={}
    # 定义词典
    dict=[]
    for content in contents :
        idf_flag=[]
        for word in content:
            if word not in dict:
                dict.append(word)
                idf_flag.append(word)
                word_counts[word]=1
            elif word not in idf_flag :
                word_counts[word]+=1
    return dict,word_counts

def calc_idf(size,dict,word_counts):
    idf=[]
    for word in dict:
        in_list=[word,size/word_counts[word]]
        idf.append(in_list )
    return pd.DataFrame(idf,columns= ['word','idf'])


if __name__ =='__main__':
    contents=[]
    with open('data/train_data.txt','r',encoding= 'utf-8') as fp:
        for line in fp.readlines():
            contents .append(line)
    # contents=['形式概念分析 可以用于设计访问控制所需要的层次结构，文献中提及的方法通常是将三维访问控制矩阵转换成二元形式背景，进行这种转换主要目的是导出形式概念、概念格结构以及角色层次和RBAC的约束。为了探索三元形式概念分析在RBAC访问控制中的应用，提出了三元形式概念分析对RBAC进行建模的方法，不必将三维访问控制矩阵转换为二元形式背景即能实现角色层次和角色责任分离。实验部分以医疗系统网络为例展示了该方法遵循RBAC角色层次和角色责任分离约束，证明了三元形式概念分析可对RBAC访问控制策略提供合理的表示。','随着物联网的不断发展,物联网的隐私保护问题引起了人们的重视,而访问控制技术是保护隐私的重要方法之一.物联网访问控制模型多基于中央可信实体的概念构建.去中心化的区块链技术解决了中心化模型带来的安全隐患.从物联网自身环境特点出发,提出物联网终端节点设备轻量级、物联网海量终端节点和物联网动态性这3个物联网下访问控制必须要解决的问题.然后,以这3个问题为核心,分析、总结了现有物联网中主流访问控制模型以及使用区块链后的访问控制模型分别是怎么解决这些问题的.最后总结出两类区块链访问控制模型以及将区块链用于物联网访问控制中的优势,并对基于区块链的物联网访问控制在未来需要 解决的问题进行了 展望.']
    cut_words_input=remove_blank_space(contents)
    print('去除空格后的文本：',cut_words_input)
    drop_stopwords_input=cut_words(cut_words_input)
    print('分词后的文本：',drop_stopwords_input)
    deal_contents_input=drop_stopwords(drop_stopwords_input)
    print('去除停用词后的文本：',deal_contents_input)
    # calc_idf_input1,calc_idf_input2=deal_contents(deal_contents_input)
    # size为文本总个数
    # size=len(contents)
    # result=calc_idf(size,calc_idf_input1,calc_idf_input2)
    # result.to_csv('data/idf.csv',header=False,index=False)
    # pos_contents(contents)