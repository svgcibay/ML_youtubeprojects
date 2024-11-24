# -*- coding: utf-8 -*-
"""Youtube ML Makina Öğremesi Ders 4.ipynb adlı not defterinin kopyası

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a1uY1M5Q065b7gl7etnxNmkFgUBdQGEg
"""

# Preprocessing And Pandas Dummy
#Get_dummies ---> kategorik sütunları, her kategori için 0 ve 1 içeren ayrı sütunlar oluşturacak şekilde dönüştürür.

import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('audi.csv')

# y= ax+b

df.head()

df=df.drop(columns=['index','href','MileageRank','PriceRank','PPYRank','Score'])

df.head()

# y= ax+b

df.info()

df.head(3)

df.columns=["yil","kasa","mil","motor","ps","vites","yakit","sahip","fiyat","ppy"]

df.head(3)

df['motor']=df['motor'].str.replace("L","") #L karakteini kaldırdık boşluk ile değiştirdik.Hala kategorisel numeric değil !

pd.to_numeric(df['motor'])

df['motor']=pd.to_numeric(df['motor'])#motor sütununu numerice veri tipine dönüştürdük

df.head(3)

df=pd.get_dummies(df,columns=['kasa','vites','yakit'],drop_first=True)
df.head()

y=df[['fiyat']]
x=df.drop("fiyat",axis=1) #axis=1 sütunlardan fiyatı sil

lm=LinearRegression()
model=lm.fit(x,y)

model.predict([[2017,30000,1.6,110,1,2600,0,1]])

model.score(x,y)

