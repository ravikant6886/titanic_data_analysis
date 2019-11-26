
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math 

titanic_data= pd.read_csv("titanic.csv")
titanic_data.head(10)
print("# of passengers in titanic ship:" +str(len(titanic_data.index)))


# In[8]:


pwd


# # anlyzing data

# In[10]:


sns.countplot(x="survived", data= titanic_data)


# In[12]:


sns.countplot(x="survived", hue="sex", data=titanic_data)


# In[13]:


sns.countplot(x="survived", hue= "pclass",data=titanic_data)


# In[14]:


titanic_data["age"].plot.hist()


# In[17]:


titanic_data["fare"].plot.hist(bins=20, figsize=(10,5))


# In[18]:


titanic_data.info()


# In[19]:


sns.countplot(x="sibsp",data=titanic_data)


# In[20]:


sns.countplot(x="body", data=titanic_data)


# In[21]:


titanic_data.isnull()


# In[23]:


titanic_data.isnull().sum()

