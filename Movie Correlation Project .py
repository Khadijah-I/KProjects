#!/usr/bin/env python
# coding: utf-8

# In[48]:


#import libraries

import pandas as pd
import seaborn as sns
import numpy as np
import re

import matplotlib
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from matplotlib.pyplot import figure 

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8) #adjusts the configuration of the plots we will create 

# read in the data 

df = pd.read_csv('/Users/khadijahiscandri/Downloads/movies.csv')


# In[15]:


# let's look at the data 

df.head()


# In[18]:


# let's see if there is any missing data 

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{}-{}%'.format(col,pct_missing))


# In[20]:


# data types for our columns

df.dtypes


# In[24]:


# change data type of columns 

df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0).astype(int)
df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(0).astype(int) 


# In[105]:


df.head()


# In[59]:


# create correct year column
# replace all locations, or alphabets using regex
df['released'] = df['released'].replace(r'[a-zA-z]', '', regex=True)


# In[61]:


# replace all parenthesis using regex
df['released'] = df['released'].replace(r'[()]', '', regex=True)


# In[65]:


# now creating yearcorrect column
df['yearcorrect'] = df['released'].astype(str).str[4:]


# In[66]:


# checking that all alterations were made
df


# In[75]:


df = df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[69]:


pd.set_option('display.max_rows', None)


# In[71]:


# dropping duplicates 
# showing all unique values
df.drop_duplicates()


# In[72]:


df.head()


# In[73]:


# predictions: budgets high correlation
# predictions: company high correlatoin 


# In[77]:


# scatter plot with budget vs gross revenue 


plt.scatter(x=df['budget'],y=df['gross'])

plt.title('Budget vs Gross Earnings')

plt.xlabel('Gross Earnings')

plt.ylabel("Budget for Film ")
plt.show()


# In[76]:


df.head()


# In[81]:


# plot the budget vs gross using seaborn

sns.regplot(x='budget',y='gross',data=df, scatter_kws={"color": "black"}, line_kws={"color": "red"})


# In[83]:


# let's start looking at correlations


# In[87]:


df.corr(method="pearson") #pearson, kendall, spearman


# In[88]:


# high correlation between budget and gross


# In[92]:


correlation_matrix = df.corr(method="pearson")

sns.heatmap(correlation_matrix, annot=True)


plt.title('Correlation Matrix')

plt.xlabel('Movie Features')

plt.ylabel("Movie Features")

plt.show()


# In[93]:


# looks at company 

df.head()


# In[106]:


df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
df_numerized.head()


# In[96]:


correlation_matrix = df_numerized.corr(method="pearson")

sns.heatmap(correlation_matrix, annot=True)


plt.title('Correlation Matrix')

plt.xlabel('Movie Features')

plt.ylabel("Movie Features")

plt.show()


# In[97]:


# filter the matrix down 
df_numerized.corr()


# In[98]:


# see the highest correlations
correlation_mat = df_numerized.corr()

corr_pairs = correlation_mat.unstack() # 

corr_pairs


# In[103]:


sorted_pairs = corr_pairs.sort_values(ascending=False)
sorted_pairs


# In[104]:


high_corr = sorted_pairs[(sorted_pairs) > 0.5]
high_corr


# In[ ]:


# votes and budgets have the highest correlation to gross earnings

#company has no correlation 

