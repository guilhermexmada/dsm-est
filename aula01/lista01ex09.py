import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Produto': ['Placa de vídeo', 'Memória RAM', 'Fonte de alimentação', 'Fan'],
    'Preco': [2700, 650, 400, 25],
    'Estoque': [12, 36, 45, 80]
}

df = pd.DataFrame(dados)

print('========= LENDO DATAFRAME =========\n')

print(f'01. Exibindo dataframe completo: \n {df}\n')
print(f'02. Exibindo primeiras linhas: \n {df.head()}\n')
print(f'03. Exibindo informações gerais: \n')
df.info()
print('\n')

print('========= CALCULANDO ESTATÍSTICAS =========\n')
print(f'03. Exibindo dados estatísticos: \n {df.describe()}\n')
print(f'04. Máximo Preço: {df['Preco'].max()}\n')
print(f'05. Mínimo Preço: {df['Preco'].min()}\n')
print(f'06. Tamanho dataframe: {len(df)}\n')
print(f'07. Soma de estoque: {df['Estoque'].sum()}\n')

print('========= CALCULANDO VALOR ESTOCADO =========\n')
df['ValorEstoque'] = df['Estoque'] * df['Preco']
print(df)

print('========= CONSTRUINDO GRÁFICO PRODUTO X PREÇO =========\n')
plt.bar(df['Produto'], df['Preco'])
plt.xlabel('Produtos')
plt.ylabel('Preços')
plt.title('Produtos de Informática')
plt.show()

print('========= CONSTRUINDO GRÁFICO PRODUTO X ESTOQUE =========\n')
plt.bar(df['Produto'], df['Estoque'])
plt.xlabel('Produtos')
plt.ylabel('Quantidade em estoque')
plt.title('Estoque Informática')
plt.show()

print('========= CONSTRUINDO GRÁFICO PRODUTO X VALOR ESTOCADO =========\n')
plt.bar(df['Produto'], df['ValorEstoque'])
plt.xlabel('Produtos')
plt.ylabel('Valor em estoque')
plt.title('Valor-Estoque Informática')
plt.show()