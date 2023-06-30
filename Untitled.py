#!/usr/bin/env python
# coding: utf-8

# # TITANIC DATASET EDA

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


titanic = pd.read_csv('tested.csv')


# In[5]:


titanic.head()


# In[6]:


titanic.isnull()


# In[7]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[8]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',data=titanic)


# In[11]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data = titanic,)


# In[12]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data = titanic,)


# In[13]:


sns.displot(titanic['Age'].dropna(),kde=False)


# In[14]:


sns.countplot(x='SibSp',data=titanic)


# In[15]:


titanic['Fare'].hist(color='red',bins=40,figsize=(8,4))


# # Data cleaning

# In[16]:


plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=titanic)


# In[18]:


titanic['Age']=titanic['Age'].fillna(titanic['Age'].mean())


# In[19]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[ ]:




