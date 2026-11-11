import pandas as pd 
import matplotlib.pyplot as plt 

notas = [7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10]

# transforma em Series
series = pd.Series(notas)

# calcula frequências
freq_absoluta = series.value_counts().sort_index()
freq_relativa = freq_absoluta / len(series)
freq_acumulada = freq_absoluta.cumsum()

# constrói tabela
frequencias = {
    'Frequência Absoluta': freq_absoluta,
    'Frequência Relativa': freq_relativa,
    'Frequência Acumulada': freq_acumulada
}
tabela = pd.DataFrame(frequencias)
print(tabela)

# constrói gráfico de barras
freq_absoluta.plot(kind='bar')
plt.xlabel('Notas')
plt.ylabel('Frequências')
plt.title('Distribuição de Notas')
plt.show()

# constrói gráfico de pizza
freq_absoluta.plot(kind='pie')
plt.ylabel('')
plt.title('Distribuição de Notas')
plt.show()