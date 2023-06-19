#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# In[ ]:





# # Introduction

# In[37]:


#import general libraries
import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 200)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import plotly.figure_factory as ff


# ## Streamlit

# In[3]:


import streamlit as st


# In[46]:


st.set_page_config(
    page_title="9base",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# ## Load Data

# In[47]:


df = pd.read_csv('C:\\Users\\b7tbu\\JUPYTER PROJECTS\\ANALYTICO\\Data_Exports\\Player\\Batting\\EXPORT_annual.csv')


# In[48]:


df.head()


# ## Scatter Chart

# In[49]:


import plotly.express as px


# In[50]:


fig = px.scatter(
    df.query("Season==2023"),
    x = "wRC+",
    y = "Hard%+",
    color = "Team",
    hover_name = "Name",
    log_x = True,
    size_max = 60,
)


# In[51]:


#st.plotly_chart(fig, theme="streamlit", use_container_width = True)


# ## Filters

# In[52]:





# In[53]:





# In[54]:





# In[55]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Columns

# In[21]:


col1, col2 = st.columns([3,1])


# In[24]:


col1.subheader("Scatter Chart")
col1.plotly_chart(fig, theme="streamlit", use_container_width = True)

col2.subheader("Filters")
col2.write(df)


# ## Print Data

# In[13]:


from st_aggrid import AgGrid


# In[14]:


st.subheader('Raw data')
AgGrid(df)


# In[ ]:





# In[ ]:




