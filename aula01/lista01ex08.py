import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Modelo': [
        'Civic',
        'Corolla',
        'Onix',
        'Gol',
        'HB20',
        'Compass',
        'Creta',
        'T-Cross',
        'Renegade',
        'Tracker'
    ],
    'Ano': [
        2022,
        2023,
        2021,
        2020,
        2022,
        2024,
        2023,
        2024,
        2021,
        2023
    ],
    'Preco': [
        125000,
        135000,
        78000,
        65000,
        82000,
        180000,
        120000,
        145000,
        110000,
        130000
    ]
}

df = pd.DataFrame(dados)

print(df) # exibe dataframe

print(df.head()) # exibe as primeiras linhas com head()

print(df.describe()) # exibe dados estatísticos relevantes com describe()

print(df.info()) # exibe informações gerais com info()

# monta e exibe gráfico
plt.bar(df['Modelo'], df['Preco'])
plt.xlabel('Modelos')
plt.ylabel('Preços')
plt.title('Carros em destaque 08/2026')
plt.show()