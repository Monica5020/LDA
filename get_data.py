import pymongo
from urllib .parse import quote_plus
db_url='mongodb://%s:%s@%s' %(quote_plus('kus'),quote_plus('kus') ,'192.168.1.115:27017' )
myclient = pymongo.MongoClient(db_url)
mydb = myclient["kus_acq"]
mycol = mydb["safe_acq"]
list=['访问控制','加密算法','鲁棒性','信息隐藏','攻击者','水印嵌入','数据备份','计算机病毒','防火墙','图像加密','隐私保护','数据安全','服务器']
for temp_type in list :
    myquery={'type':temp_type}
    temp_list=[]
    myresult = mycol.find(myquery)
    for x in myresult:
        temp_list.append(x)

    all=len(temp_list)
    train_i=int(0.4*all)
    test_i=int(0.9*all)

    fp_train=open(r'E:\import_db\train_data.txt','a',encoding= 'utf-8')
    for y in temp_list[0:train_i]:
        fp_train.write(y['content']+5*y['keywords'])
        fp_train.write('\n')
        fp_train.flush()
    fp_train.close()

    fp_test=open(r'E:\import_db\test_data.txt','a',encoding= 'utf-8')
    for z in temp_list[test_i:]:
        fp_test.write(z['content']+5*z['keywords'])
        fp_test.write('\n')
        fp_test.flush()
    fp_test.close()
    print(temp_type ,'写入完毕！')

print('完成！')