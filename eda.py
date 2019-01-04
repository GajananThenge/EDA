# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:13:39 2018

@author: gajanan.thenge
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('bmh')

df = pd.read_csv('./Master Data/Reservoir C.csv')
df.head()

#df2=df
#del df2['Country ID']
#del df2['Project ID']
#del df2['Site ID']



df1 = df[["Volume","Temperature","Precipitation","Humidity"]]


print(df2['Volume'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(df1['Volume'], color='g', bins=100, hist_kws={'alpha': 0.4});

list(set(df1.dtypes.tolist()))

df_num = df1.select_dtypes(include = ['float64', 'int64'])
df_num.head()



df_num.hist(figsize=(8, 10), bins=50, xlabelsize=8, ylabelsize=8)

df_num_corr = df_num.corr()['Volume'] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Volume:\n{}".format(len(golden_features_list), golden_features_list))


for i in range(0, len(df_num.columns)):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i],
                y_vars=['Volume'],height=7)
    
