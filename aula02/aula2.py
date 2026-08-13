import pandas as pd 

dados = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Gabinete", "Headset", "Webcam", "HDMI", "Cooler"],
    "Preço": [85, 150, 980, 220, 320, 123, 566, 90],
    "Quantidade": [12, 8, 4, 10, 6, 4, 20, 10] 
}

df = pd.DataFrame(dados)

df['ValorTotal'] = df['Preço'] * df['Quantidade'] # cria e atribui nova coluna multiplicando outras 2

print(df.sort_values('ValorTotal')) # exibe dataframe ordenado pela nova coluna

print('\n === \n')

print(df['Quantidade'] < 10) # cria coluna-filtros com base na quantidade

print('\n === \n')

print(df[df['Quantidade'] < 10]) # retorna as linhas filtradas

print('\n === \n')

print(df[(df['Quantidade'] > 10) & (df['Preço'] > 100)]) # combina condições