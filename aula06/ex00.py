import pandas as pd

tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

media_aritmetica = tempos.mean()

mediana = tempos.median()

moda = tempos.mode()

maximo = tempos.max()

minimo = tempos.min()

print(f'dados: {tempos}; \nmédia: {media_aritmetica}; \nmediana: {mediana}; \nmoda: {moda}; \nmáximo: {maximo}; \nmínimo: {minimo}')

print('\nComo o conjunto de dados não possui outliers, a média aritmética pode representar bem')