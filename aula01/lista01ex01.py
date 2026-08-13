# cadastro de alunos
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Alunos" : ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "Idades" : [18,20,19,22,21,18,23,20]
}

df = pd.DataFrame(dados)

print(df) # exibe o dataframe

print(df.head()) # exibe as 5 primeiras linhas

df.info() # exibe informações do dataframes

print(df.describe()) # exibe resumo estatístico