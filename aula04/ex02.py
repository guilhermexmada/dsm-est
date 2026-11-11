import pandas as pd
import matplotlib.pyplot as plt

langs = ['python','python','python','java','javascript','java','javascript','typescript','c','go','php','c','c','c#','c++','ruby','ruby','assembly','rust','go','php','java','javascript','java','javascript','typescript','ruby','assembly','visual basic','cobol','swift','visual basic','dart','lua','dart','lua','kotlin','objective-c','r','shell','scala']
series = pd.Series(langs) # transforma lista em Series

# calcula frequências absoluta e relativa
freq_absoluta = series.value_counts().sort_index()
freq_realtiva = freq_absoluta / len(series)

# printa linguagem mais frequente
print(f'{freq_absoluta.idxmax()} | {freq_absoluta.max()}')

# constrói gráfico de barras
freq_absoluta.plot(kind='bar')
plt.ylabel('')
plt.title('Distribuição das linguagens')
plt.show()