import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Filme': ['Avatar','Matrix','Interestelar','Vingadores','Barbie'],
    'Nota': [9.2,9.5,9.8,8.9,7.5]
}

df = pd.DataFrame(dados) # cria dataframe

print(df.head()) # exibe as primeiras linhas com head()

print(df.describe()) # exibe dados estatísticos relevantes com describe()

# monta e exibe gráfico
plt.bar(df['Filme'], df['Nota'])
plt.xlabel('Filmes')
plt.ylabel('Notas')
plt.show()