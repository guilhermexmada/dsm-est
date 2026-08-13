import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Time': ['Palmeiras','Flamengo','Corinthians','São Paulo','Santos'],
    'Pontos': [48,46,41,38,35]
}

df = pd.DataFrame(dados) # cria dataframe

# monta e exibe gráfico
plt.bar(df['Time'], df['Pontos'])
plt.xlabel('Times')
plt.ylabel('Pontos')
plt.title('Líderes do Campeonato Brasileiro')
plt.show()