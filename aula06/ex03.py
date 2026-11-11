import pandas as pd
import matplotlib.pyplot as plt

tempos = pd.Series([100, 105, 110, 108, 115, 120, 125, 130, 500, 550])

media = tempos.mean()
mediana = tempos.median()
moda = tempos.mode()
maxi = tempos.max()
mini = tempos.min()

print('média: ', media)
print('mediana: ', mediana)
print('moda: ', moda)
print('máximo: ', maxi)
print('mínimo: ', mini)

hist = tempos.hist(bins=6)

plt.xlabel("Frequências")
plt.ylabel("Valores")
plt.title("Distribuição dos Tempos de Requisição")
plt.show()