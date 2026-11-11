import pandas as pd 
import matplotlib.pyplot as plt 

notas = [5, 6, 7, 8, 9, 10]
frequencias = [2, 3, 5, 6, 3, 2]

# gráfico de barras com Matplotlib

plt.bar(notas, frequencias) # cria o gráfico com 2 eixos
plt.xlabel("Nota") # nomeia o eixo X
plt.ylabel("Frequência") # nomeia o eixo Y
plt.title("Distribuição das Notas") # define o título
plt.show() # exibe

# gráfico de barras com Pandas