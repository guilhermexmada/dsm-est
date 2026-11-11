import pandas as pd 
import matplotlib.pyplot as plt

tempos = [
    120, 145, 98, 210, 175,
    132, 160, 115, 185, 250,
    105, 140, 195, 155, 130,
    300, 125, 170, 145, 110,
    220, 135, 180, 95, 165,
    155, 200, 125, 140, 190,
    115, 280, 150, 130, 175,
    105, 160, 145, 230, 120,
    185, 135, 170, 110, 155,
    320, 140, 125, 195, 150
]

series = pd.Series(tempos)

freq_abs = series.value_counts().sort_index()

plt.hist(freq_abs, bins=5)
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")
plt.show()

plt.hist(freq_abs, bins=3)
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")
plt.show()

plt.hist(freq_abs, bins=10)
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")
plt.show()