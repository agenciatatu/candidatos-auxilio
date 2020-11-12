#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
from sqlalchemy import create_engine

print (pd.read_csv("202008_AuxilioEmergencial.csv", nrows=5, encoding='latin1', sep=';')) #imprime apenas para visualizacao das primeiras linha



# In[ ]:


csv_database = create_engine('sqlite:///emergencial.db')

chunksize = 100000 #limita uso da memoria
i = 0
j = 1
for df in pd.read_csv("202008_AuxilioEmergencial.csv", chunksize=chunksize, iterator=True, encoding='latin1', sep=';'): #SEP E LINETERMINATOR É POR CONTA DA TABULAÇÃO DO CSV
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
      df.index += j
      i+=1
      df.to_sql('table', csv_database, if_exists='append')
      j = df.index[-1] + 1

