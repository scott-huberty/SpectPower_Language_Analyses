#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install statsmodels


# In[1]:


import statsmodels.api as sm


# In[2]:


import statsmodels.formula.api as smf


# In[3]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_stata('DQPlots_stata.dta')


# In[4]:


type(df)


# In[5]:


df.head()

