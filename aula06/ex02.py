import pandas as pd

salarios = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 20000])

media = salarios.mean()

mediana = salarios.median()

moda = salarios.mode()

print('média: ', media)
print('mediana: ', mediana)
print('moda: ', moda)

print('A média salarial não representa bem o conjunto de salários pela preseça do outlier 20000. Esse valor sozinho puxou a média para cima. A melhor medida nesse caso seria a mediana.')