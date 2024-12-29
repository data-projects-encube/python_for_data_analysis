#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:\\python_for_data_analysis\\archive\\API_ILO_country_YU.csv")
data.head(10)
data.shape
data.columns
data.tail(10)

#want to analyse only for 2010 to 2012. Use iloc(column index location to filter required columns)
data_3yr=data.iloc[:,[0,1,2,3,4]].copy()
data_3yr

#data cleaning
#find null values
data_3yr.isnull().sum()
data_3yr.dropna(how='all',subset=['2010','2011','2012'],inplace=True)
data_3yr.isnull().sum()
#check data types
data_3yr.dtypes
#sort by country
data_3yr.sort_values('Country Name')
#set country code as index
data_3yr.set_index('Country Code',inplace=True)
data_3yr

#add 3 years average
data_3yr['3yrs_avg']=data_3yr[['2010','2011','2012']].mean(axis=1)
data_3yr
data_3yr['2010-11_YOY_Diff']=data_3yr['2011']-data_3yr['2010']
data_3yr

#sort by uemp rate
top_10_countries_high_uemp=data_3yr.sort_values('3yrs_avg',ascending=False)[0:10].copy()
top_10_countries_high_uemp

#top 5 uemp
top_5_countries_high_uemp=data_3yr.sort_values('3yrs_avg',ascending=False)[0:5].copy()
top_5_countries_high_uemp

#Plot
uemp=top_10_countries_high_uemp['3yrs_avg']
countries=list(top_10_countries_high_uemp.index)
fig,ax=plt.subplots(nrows=1,ncols=1)
ax.bar(countries,uemp)

plt.xlabel('Country Code',fontsize=10)
plt.ylabel('3 Years average unemployment rate',fontsize=10)
plt.xticks(rotation='vertical',fontsize=10)

ax.grid()
plt.show()





