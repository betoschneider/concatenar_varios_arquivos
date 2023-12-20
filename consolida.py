import pandas as pd
from os import listdir

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

#nome do arquivo com dados concatenados
arquivo_consolidado = '%s\dados_consolidados.csv' % (pasta)

try:
    #abrir arquivo com dados concatenados
    df_consolidado = pd.read_csv(arquivo_consolidado)
    #adiciona novos dados (dataframe temporário)
    df_consolidado = pd.concat([df_consolidado, df_consolidado_temp], ignore_index=True)
    #exportar dataframe com novos dados para csv
    df_consolidado.to_csv(arquivo_consolidado, sep=',')
except:
    #caso não exista arquivo com dados concatenados
    #exportar dataframe temporário com novos dados para csv
    df_consolidado_temp.to_csv(arquivo_consolidado, sep=',', index=False)

