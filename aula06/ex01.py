import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10])

media = notas.mean()

mediana = notas.median()

moda = notas.mode()

maximo = notas.max()

minimo = notas.min()

print(f'\n media: {media} \n mediana: {mediana} \n moda: {moda} \n máximo: {maximo} \n mínimo: {minimo}')

print('\nComo o conjunto é numeroso e não apresenta outliers, a média é eficiente')