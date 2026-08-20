import numpy as np 
import pandas as pd

np.random.seed(20)

dados = {
    'Notas': np.random.normal(70, 10, 10000) # 10 mil registros, média aprox. 70, desvio padrão 10
}

df = pd.DataFrame(dados)

print(df.head())

print('\n===||===||===||===\n')

print(df['Notas'].mean())

print('\n===||===||===||===\n')

for tamanho in [10, 50, 100, 500, 1000]:
    amostra = df.sample(n=tamanho, random_state=14)
    media = amostra['Notas'].mean()
    print(media)