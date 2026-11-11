import pandas as pd
import matplotlib.pyplot as plt

notas = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 7, 8, 9, 10, 8, 7, 6, 8, 9, 8] 
serie = pd.Series(notas) 

frequencia = serie.value_counts().sort_index() # armazena frequências
frequencia.plot(kind="pie", autopct='%1.1f%%') # define tipo "de pizza"

plt.title("Distribuição das Notas") # define título
plt.ylabel("") 
plt.show() # exibe