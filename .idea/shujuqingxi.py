import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
df = pd.read_csv('F:\longkong\.idea\he.csv',encoding="gbk",low_memory=False)
obj = pd.DataFrame(df)
lie = obj.columns
'''
第一步：去重
duplicated()函数查找dataform数据中重复的数据，所有列的值都匹配确认，重复返回true。
drop_duplicates()函数查找后，去除重复数据
'''
obj = obj.drop_duplicates()
print(obj)# 根据结果，有十行数据重复。数据去重后，索引不变，最后要重新创建索引。
'''
第二步,处理数据中的空值
isnull()函数，如果是空值就显示True。
notnull()函数正好相反，如果是空值就显示False。
可通过value_counts()函数进行统计。
对于空值有两种处理的方法：
第一种是使用fillna()函数对空值进行填充，可以选择填充0值或者其他任意值。
第二种方法是使用dropna()函数直接将包含空值的数据删除。
建议填充替换，不去改变表结构，可以估计值进行填充。
根据这次爬取的内容，表有五列数据，有四列不能为空，最后一列name可为空。
'''
t1 = obj['title'].isnull().value_counts()
t2 = obj['author'].isnull().value_counts()
t3 = obj['data'].isnull().value_counts()
t4 = obj['heat'].isnull().value_counts()
t5 = obj['name'].isnull().value_counts()
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)#根据结果，第二三四列数据没有空值，但是第一列有2个空值，我只能丢弃这两行的数据。
obj = obj[(True-df['title'].isin([np.nan]))]
print(obj)#数据表还有5818行数据
'''
第三步，处理数据的极端值与异常值。
在数据表最后一列里面有些异常值，不是我们想要的书名，是一些乱码字符串，我们对其整行数据进行删除。
因为要根据name列数据的内容进行判断，然后在处理。
我打算先用正则表达式匹配找到乱码的行，再删除,re.search(pattern, string, flags=0)。
因为乱码内容，是由于抓取数据时，匹配不严格，乱码多为href标签网址。
'''
for i in obj['name']:
    if re.search('href',str(i)) is not None:
        obj = obj[(True-df['name'].isin([i]))]
print(obj)#异常值处理完毕，数据表内容还有5682行。
'''
第四步，更改数据格式
由于数据都是从页面抓取得到的，数据格式都是python型，也就是字符型。
data数据列应为日期型，需修改。
heat数据列应为数字型，需修改。
更改和规范数据格式，所使用的函数是astype()。
对heat列中的数据，通常为整数，因此我们数据格式改为int64。
在数据格式中还要特别注意日期型的数据。日期格式的数据需要使用to_datatime函数进行处理。
'''
obj['heat']=obj['heat'].astype(np.int64)
obj['data']=pd.to_datetime(obj['data'])
print(obj.dtypes)#数据表中数据的清洗基本完毕
'''
最后一步，重新建立索引
'''
obj = obj.reset_index(drop=True)
print(obj)#数据表重新建立索引，共5682行。
'''
重新存储为csv文件。
'''
obj.to_csv('F:\longkong\shuju.csv')

