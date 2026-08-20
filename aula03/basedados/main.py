import pandas as pd

# cria um dataframe a partir do arquivo de dados
df = pd.read_csv('dados.csv')

# descobre população
print(f'População: {df.shape[0]}')

# visualiza primeiros elementos
print(f'Primeiros elementos: \n===\n{df.head()}\n===\n')

# seleciona amostra
qtd = 10
amostra = df.sample(n=qtd)
# amostra = df.sample(n=qtd, random_state=20) <- descomente para usar amostragem fixa
print(f'Amostra de {qtd} elementos: \n===\n{amostra}\n===\n')

# compara população x amostra
mediaPop = df['idade'].mean()
mediaAm = amostra['idade'].mean()
erroAmostral = mediaPop - mediaAm
print(f'Média idade população: {mediaPop}\n')
print(f'Média idade amostra: {mediaAm}\n')
print(f'Erro amostral: {erroAmostral:.2f}\n')