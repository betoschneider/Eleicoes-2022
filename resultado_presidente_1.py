# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:11:23 2022

@author: Roberto Schneider
"""


import pandas as pd
from datetime import datetime
import time

df_candidatos = None

arquivo = 'resultado.xlsx'

#1o turno
link_resultado = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
#2o turno
link_resultado = 'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'

base =  pd.read_json(link_resultado)

while True:
    for i in base['cand']:
        #cria dataframe com a fotografia atual da apuração
        temp = pd.DataFrame([i])
        #busca hora da disponiblização do resultado no link
        #caso vazio, busca hora atual
        try:
            hora = '%s %s' % (base['dt'].max(), base['ht'].max())
            hora = pd.to_datetime(hora, format='%d/%m/%Y %H:%M:%S')
        except:
            hora = datetime.now()
        
        #cria coluna com data e hora
        temp['dt_hr_atualiza'] = hora
        
        #concatena ultima fotografia com base histórica
        df_candidatos = pd.concat([df_candidatos, temp], ignore_index=True)
    
    try:
        base_historica = pd.read_excel(arquivo)
        df_candidatos = pd.concat([base_historica, df_candidatos], ignore_index=True)
    except:
        pass
    
    #remove registros duplicados
    df_candidatos.drop_duplicates(inplace=True)
    
    
    #exporta base histórica para excel
    df_candidatos.to_excel(arquivo, index=False)
    
    #imprime na tela
    print(link_resultado)
    #imprime ultima fotografia
    print(df_candidatos[['n', 'nm', 'pvap', 'vap', 'dt_hr_atualiza']][(df_candidatos['dt_hr_atualiza'] == hora)])
    
    #aguarda tempo em segundos para a próxima consulta
    time.sleep(60)


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