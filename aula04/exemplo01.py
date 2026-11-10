import pandas as pd

notas = [
    7, 8, 6, 9, 7,
    5, 8, 7, 10, 6,
    8, 9, 7, 5, 6,
    8, 7, 9, 8, 10
]

# dataframe = tabela
# series = coluna

serie = pd.Series(notas) 

print(serie)
print(serie.value_counts())
print(serie.value_counts().sort_index()) # ordena pelo valor (no caso, pela nota)
print(serie.value_counts().sort_values()) # ordena pela frequência (da menor pra maior frequência)
print(serie.value_counts(normalize=True) * 100) # transforma em frequência relativa
frequencia = serie.value_counts()
frequenciaAcumulada = frequencia.cumsum() # calcula freq acumulada para um conjunto de dados
print(frequenciaAcumulada)

tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "FrequenciaRelativa": frequencia / len(serie),
    "FrequenciaAcumulada": frequenciaAcumulada
})

print(tabela)