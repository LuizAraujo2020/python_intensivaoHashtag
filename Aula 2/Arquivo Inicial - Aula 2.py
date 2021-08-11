#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[2]:


# Passo 1: Importar a base de dados pro Python
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")
display(tabela)


# In[3]:


# Passo 2: Visualizar a DB
# Entender quais informações vc tem disponível
# descobrir as cagadas da DB

tabela = tabela.drop("Unnamed: 0", axis=1) #drop apaga #0=linha 1=coluna
display(tabela)


# In[13]:



# Passo 3: Tratamento da DB
#  Valores numéricos que o python acha que é texto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#  Valores vazios
#     #colunas vazias
tabela = tabela.dropna(how="all", axis=1) #drop só apaga vazios
# all para excluir colunas onde todos os valores sao vazios
# any para excluir colunas onde pelo menos 1 vazio

#     #linhas vazias
tabela = tabela.dropna(how="any", axis=0)# dropna axis=0 = dropa alguma linha com valor vazio

display(tabela.info())

#  excluir informações inúteis 


# In[21]:



# Passo 4: Análise exploratória -> Análise Geral -> Ver como estão os cancelamentos 
display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[25]:


# Passo 5: Olhar as colunas da nossa DB -> Identificar o Motivo  dos clientes cancelarem
# procurar info que saltam aos olhos, pois o que faz cancelar salta aos olhos
import plotly.express as px

coluna = "MesesComoCliente"
#passos pra criar gráfico:
    #1 criar
    #2 exibir
grafico = px.histogram(tabela, x=coluna, color="Churn")
display(grafico)



# In[28]:


#para edicoes plotly.com/python/histograms/


for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    display(grafico)
    


# ### Conclusões e Ações

# In[ ]:





# Escreva aqui suas conclusões:
# - Clientes com famílias maiores (casados e com dependentes) tendem a cancelar menos
#     - Será que não vale dar bonus para filhos ou esposa
# - MesesComoCliente baixo tem muito, mas MUITO mais chances de cancelar
#     - Talvez a 1a experiencia está sendo ruim.
#     - Talvez está trazendo clientes desqualificados
#     - Ideia: pode ser interessante criar programa de incentivo ao cliente nos primeiros meses;
# - Clientes de FIbra tem uma taxa de cancelamento muito alta:
#     - Temos que verificar o serviço de Fibra
# - Quanto mais servicos o cliente tem, menor a chance de cancelar:
#     - Oportunidade GIgantesca: criar um programa de incentivo aos outros serviços
# - Quase todos os cancelamentos estão no contrato mensal:
#     - Plano de incentivo aos contrato anual ou 2 anos -> vamos dar descontos para contratos anuais/bienais;
# - Evitar boleto eletrônico:
#     - Incentivar os clientes a mudarem para outras formas de pagamento

# In[ ]:




