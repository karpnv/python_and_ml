import pandas as pd
import numpy as np

a=pd.Series([1,3,5,np.nan,6,8])
b=pd.Series(['first','second','3','4','5','6'])
df2=pd.DataFrame({"A":a, "B":b})
print(df2)

df1=pd.read_csv('df.tsv', sep='\t', header=0)
#df1.Name
# for person in df1['Name']:
#     print(person)
#
# for col in df1:
#     print(df1[col])
#dtypes
#df1.Birth=df1.Birth.apply(pd.to_datetime)
#print(df1.info())
#info
#sB=df1.fillna('стажер').Position
#print(type(sB))
#df1.Position - series
#df1[['Position','Name']] - DataFrame
#print(df1.head(2))
#head(3)
#print(df1)
#[-3:]
# df2=df1.iloc[0:3,0:2]
# df2=df1.iloc[0:3,[1,2]]
#print(df2)
#loc[[1,3,5],['Name','City']])
#loc[[1,3,5],[2,3]])
#ix[]
#df2=df1.ix[0:3,0:2]
#df2=df1.ix[0:3,[1,2]]
#print(df2)
#df2=df1[(df1.Birth<pd.datetime(1986,11,22))&(df1.City!='Москва')]
#print(df2[['Name','City']])
#print(df1)
#df1[(df1.Birth>pd.datetime(1985,1,1))&(df1.City!='Москва')]
#df1[(df1.Birth>pd.datetime(1985,1,1))|(df1.City!='Волгоград')]
#df1[4,'Position']='старший инженер'

#df1['IsStudent'] = [False,True, False, True, False, True]
#df1[['Name','Position']]
#print(df1.join(df1[['Name','Position']],lsuffix='_suf', on='Name'))
#df1.to_csv('df2.csv')
# print(df1)

# from sklearn import datasets
# data=datasets.load_iris()
# print(data.data)
