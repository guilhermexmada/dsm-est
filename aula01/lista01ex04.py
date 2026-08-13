import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Produto': ['Arroz','Feijão','Café','Açúcar','Leite','Óleo','Macarrão'],
    'Preço': [32,11,24,6,8,9,7]
}

df = pd.DataFrame(dados) # cria dataframe

plt.bar(df['Produto'], df['Preço']) # monta gráfico 

plt.title('Produtos Precificados') # altera título

# nomeia eixos
plt.xlabel('Produtos cotados')
plt.ylabel('Preços atualizados')

# exibe gráfico
plt.show()