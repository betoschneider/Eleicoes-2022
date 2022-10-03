# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:11:23 2022

@author: Roberto Schneider
"""


import pandas as pd

base =  pd.read_json('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

df_candidatos = None
for i in base['cand']:
    #temp = pd.DataFrame.from_dict(i, orient='columns').reset_index()
    temp = pd.DataFrame([i])
    df_candidatos = pd.concat([df_candidatos, temp], ignore_index=True)

df_candidatos_resumo = df_candidatos[['n', 'nm', 'pvap', 'vap']]
print(df_candidatos_resumo)


'''
colunas da tabela base


dt ultima atualizacao = 'dt'
hora da ultima atualizacao = 'ht'

total de secoes = 's'
total de secoes totalizadas = 'st'
% de secoes totalizadas = 'pst'
total de secoes nao totalizadas = 'snt'
% de secoes nao totalizadas = 'psnt'
qtd votos = 'c'
% votos = 'pc'
qtd abstencao = 'a'
% abstencao = 'pa'
qtd votos validos = 'vv'
% votos validos = 'pvv'
qtd votos brancos = 'vb'
% votos brancos = 'pvb'
qtd votos nulos = 'tvn'
% votos nulos = 'ptvn'
qtd votos anulados sub judice = 'vansj'
% votos anulados sub judice = 'pvansj'
qtd votos anulados e apurados em separado = 'van'
% votos anulados e apurados em separado = 'pvan'
qtd total de votos = 'tv'

'''