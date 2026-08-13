# loja de informatica
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "Preço": [85, 150, 980, 220, 320],
    "Quantidade": [12, 8, 4, 10, 6] 
}

df = pd.DataFrame(dados)

print(f'Quantidade de produtos: {len(df["Produto"])}')

print(f'Produto mais caro: {df['Preço'].max()}') 

df_preco_ascendente = df.sort_values('Preço')

df_preco_descendente = df.sort_values('Preço', ascending=False)

print(f'Produto mais caro: {df_preco_descendente.iloc[0, 0]}')

print(f'Produto mais barato: {df_preco_ascendente.iloc[0, 0]}') 

print(f'Soma das quantidades: {df['Quantidade'].sum()}') 


