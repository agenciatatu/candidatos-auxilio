#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:


#Cruza as bases de dados dos bens dos candidatos com a base contendo o cpf dos candidatos
dfbens = pd.read_csv('JupyterNotebook/bem_candidato_2020_AL.csv')
dfnomecand = pd.read_csv('JupyterNotebook/nomes_candidatos2020.csv')


# In[16]:


#une as duas tabelas pela coluna SQ_CANDIDATO

dfcandidatos = pd.merge(dfnomecand, dfbens, on='SQ_CANDIDATO')


# In[ ]:





# In[37]:


# Importa para um dataframe os dados do auxílio emergencial

import sqlite3

con = sqlite3.connect("JupyterNotebook/emergencial.db")
dfauxilio = pd.read_sql_query("SELECT * from 'table' WHERE UF LIKE 'al'", con)


# In[38]:


dfauxilio


# In[17]:


#Cria cópia de DF candidatos e altera campo CPF para ser cruzado com auxílio emergencial

dfcandidatos2 = dfcandidatos.copy()


# In[18]:


#preenche NR_CPF_CANDIDATO com os zeros à esquerda

# converting to string dtype 
dfcandidatos2["NR_CPF_CANDIDATO"]= dfcandidatos2["NR_CPF_CANDIDATO"].astype(str) 
  
# width of output string 
width = 11
  
# calling method and overwriting series 
dfcandidatos2["NR_CPF_CANDIDATO"]= dfcandidatos2["NR_CPF_CANDIDATO"].str.zfill(width) 
  


# In[32]:


# cria campo com cpf mascarado igual ao do auxílio emergencial

dfcandidatos2["CPFBENEFICIÁRIO"]= "***." + dfcandidatos2["NR_CPF_CANDIDATO"].str[3:6] + "." + dfcandidatos2["NR_CPF_CANDIDATO"].str[6:9] + "-**"


# In[42]:


#Cria cópia do campo nome com header igual ao do outro df

dfcandidatos2['NOMEBENEFICIÁRIO'] = dfcandidatos2['NM_CANDIDATO'].copy()


# In[33]:


dfcandidatos2


# In[43]:


#Vincula os dois DFs

#dfauxilio_candidatos = pd.merge(dfcandidatos2, dfauxilio, on='CPFBENEFICIÁRIO')

dfauxilio_candidatos = dfcandidatos2.merge(dfauxilio, on=['CPFBENEFICIÁRIO', 'NOMEBENEFICIÁRIO'])


# In[44]:


dfauxilio_candidatos


# In[45]:


dfauxilio_candidatos.to_csv('auxilio_candidatos.csv')


# In[ ]:





# In[ ]:





# In[ ]:




