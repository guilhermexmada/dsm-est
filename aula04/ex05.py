import pandas as pd 
import matplotlib.pyplot as plt 

tempos = [ 110, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180,
 185, 190, 195, 200, 205, 210, 220, 230, 250, 300, 500 ]

plt.hist(tempos, bins=5)
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")
plt.show()

plt.boxplot(tempos)
plt.ylabel("Tempo (ms)")
plt.title("Distribuição do Tempo de Resposta")
plt.show()

print('')