import matplotlib.pyplot as plt

# um histograma mostra como os valores numéricos estão distribuídos em intervalos

# enquanto gráficos de barras mostram categorias e grupos de valores, histogramas mostram distribuição de dados numéricos e os intervalos entre os valores

idades = [18, 19, 20, 21, 22, 25, 27, 30, 31, 35]
plt.hist(idades)
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.title("Distribuição das Idades")
plt.show()

# você também pode agrupar os dados em intervalos chamados de CLASSES ou BINS

tempos = [
 120, 130, 115, 140, 150,
 180, 175, 190, 210, 220,
 250, 280, 300, 320, 350
]

plt.hist(tempos, bins=5)
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")
plt.show()