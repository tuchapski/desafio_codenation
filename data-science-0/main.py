#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head()
df = black_friday


# In[5]:


df.head()


# In[6]:


df.info()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[7]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return df.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[51]:


def q2():
    # Retorne aqui o resultado da questão 2.
    female_filtered = df.loc[(df['Age'] == '26-35') & (df['Gender'] == 'F')]
    return int(female_filtered.shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[52]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return df['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return df.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[19]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return (df.shape[0] - df.dropna().shape[0]) / df.shape[0]


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[21]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(df.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[22]:


def q7():
    # Retorne aqui o resultado da questão 7.
    cleaned_column = df['Product_Category_3'].dropna()
    return cleaned_column.mode()[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[34]:


def q8():
    # Retorne aqui o resultado da questão 8.
    min_max = (df['Purchase'] - df['Purchase'].min())             / (df['Purchase'].max() - df['Purchase'].min())
    return float(min_max.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[11]:


def q9():
    # Retorne aqui o resultado da questão 9.
    df_normalized = (df['Purchase'] - df['Purchase'].mean()) / df['Purchase'].std()
    return int(df_normalized.between(-1,1).sum())

q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[29]:


def q10():
    # Retorne aqui o resultado da questão 10.
    df_aux = df[['Product_Category_2','Product_Category_3']]
    df_aux = df_aux[df_aux['Product_Category_2'].isna()]
    return df_aux['Product_Category_2'].equals(df_aux['Product_Category_3'])

