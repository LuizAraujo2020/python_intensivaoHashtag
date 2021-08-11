#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[73]:


# Passo a passo: como eu faria isso na mão:
# Passo 1 - Entrar no sistema (entrar no link: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing)
# Passo 2 - Navegar no sistema (entrar na pasta Exportar)
# Passo 3 - Baixar o arquivo de vendas
# Passo 4 - Calcular faturamento e quantidade de produtos vendidos
# Passo 5 - Enviar o email para a diretoria

import pyautogui
import pyperclip # para digitar char especiais ? e etc, copiar texto exatamento como é
import time

pyautogui.PAUSE = 1 #diz pra esperar 1s antes de cada comando

# Passo 1

# Pode dar erro por causa de char especiais
# pyautogui.hotkey('command','t')
# pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing") 
# pyautogui.press('return')

#pra quem usa MAC
pyautogui.hotkey('command','t')
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
pyperclip.copy(link) #permmite copiar um texto (crtl+c)
pyautogui.hotkey('command', 'v')
pyautogui.press('return')


# pyautogui.hotkey('ctrl','shift', 'j')
# pyautogui.click
# pyautogui.write
# pyautogui.press('win') #tecla windows

# Passo 2
time.sleep(5) #esperar 5s só aqui
# pyautogui.click(x=351, y=391)
pyautogui.click(x=351, y=391)
pyautogui.press('return')
# pyautogui.doubleClick()
# pyautogui.doubleClick(x=351, y=391)
# pyautogui.click(x=351, y=391, button='right')

# Passo 3
time.sleep(5)
pyautogui.click(x=374, y=391)
pyautogui.click(x=888, y=199)
pyautogui.click(x=599, y=637)
time.sleep(5)
pyautogui.press('return')
time.sleep(5)


# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

# In[74]:


# Passo 4
import pandas as pd # sempre que quiser usar db, usar o pandas

tabela = pd.read_excel("Vendas - Dez.xlsx")
# tabela = pd.read_excel(r"C:\Users\blabla\Download\Vendas - Dez.xlsx")#r para usar raw, ignorar o scape sequence

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(faturamento)
print(quantidade)

display(tabela)


# ### Vamos agora enviar um e-mail pelo gmail

# In[75]:


# Passo 5

pyautogui.hotkey('command','t')
link = "https://mail.google.com/mail/u/0/#inbox"
pyperclip.copy(link) #permmite copiar um texto (crtl+c)
pyautogui.hotkey('command', 'v')
pyautogui.press('return')


time.sleep(5)
pyautogui.click(x=93, y=219)
link = "luizcarlos_bsb2006@hotmail.com"
pyperclip.copy(link) #permmite copiar um texto (crtl+c)
# pyautogui.write(link)
pyautogui.hotkey('command', 'v')
pyautogui.press('tab')
# pyautogui.press('tab')

# 3 assunto
assunto = "Relatório Mensal"
pyperclip.copy(assunto) #permmite copiar um texto (crtl+c)
pyautogui.hotkey('command', 'v')
pyautogui.press('tab')

mensagem = f"""
Olá, prezados. Bom dia!
O faturamento foi: {faturamento:,.2f}
A quantidade de vendas: {quantidade:,}
"""
pyperclip.copy(mensagem) #permmite copiar um texto (crtl+c)
pyautogui.hotkey('command', 'v')


pyautogui.hotkey('command', 'return')


# #### Use esse código para descobrir qual a posição de um item que queira clicar
# 
# - Lembre-se: a posição na sua tela é diferente da posição na minha tela

# In[76]:


import time
time.sleep(5)
pyautogui.position()#pegar a posicao do mouse


# In[ ]:




