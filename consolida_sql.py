import pandas as pd
from os import listdir
from banco import inserir_item, listar_itens, excluir_item

#local dos arquivos
pasta = r'C:\consolida'

#lista os arquivos xlsx na pasta
lista_arquivos = [arquivo for arquivo in listdir(pasta) if 'xlsx' in arquivo]

#dataframe temporário para concatenar os arquivos
df_consolidado_temp = None

#percorre a lista de arquivos, abrindo e concatenando ao dataframe temporário
for arquivo in lista_arquivos:
    df_temp = pd.read_excel('%s\%s' % (pasta, arquivo))
    df_consolidado_temp = pd.concat([df_consolidado_temp, df_temp], ignore_index=True)

#adiciona no banco de dados cada linha do nosso df consolidado
for i, linha in df_consolidado_temp.iterrows():
    inserir_item(linha['ITEM'], linha['VALOR'])

#df com os dados no banco
dados_no_bd = listar_itens()

