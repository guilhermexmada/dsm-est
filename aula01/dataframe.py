# criando meu primeiro dataframe
import pandas as pd

dados = {
    "Aluno": ["Rogério", "Matheus", "Camila", "Geovana"],
    "Nota": [8, 5, 9, 6]
}

df = pd.DataFrame(dados) # cria dataframe (tabela) preenchida com os dados

print(df) # exibe dataframe completo

print(len(df)) # exibe tamanho do dataframe (quantidade de registros/entradas)

print(df.shape) # exibe quantidade de linhas e colunas do dataframe

df.info() # retorna dados básicos do dataframe (printa automaticamente)

print(df.describe()) # monta cálculos básicos sobre o dataframe

print(df.head()) # organiza os dados visualmente em uma tabela, exibindo as primeiras linhas


