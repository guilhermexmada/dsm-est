import pandas as pd

# cria dataframe a partir do arquivo de dados
df = pd.read_csv('dados.csv')

# revela início da estrutura da base de dados
# print(df.head)

# extrai coluna com índice "idade"
serie = df['idade']

# exibe idades dos clientes
# print(serie)

# calcula frequência absoluta p/ todas as idades
fa = serie.value_counts()

# ordena frequências absolutas pela idade
fa = fa.sort_index()

# exibe frequências absolutas
# print(fa)

# calcula frequência relativa p/ todas as idades
fr = serie.value_counts(normalize=True)

# ordena frequências relativas pela frequência
fr = fr.sort_values()

# transforma frequências relativas em porcentagem
frper = fr * 100

# exibe frequências relativas em porcentagem
# print(frper)

# calcula frequência acumulada p/ todas as idades
fac = serie.value_counts().cumsum()

# ordena frequências acumuladas pela frequência
fac = fac.sort_values()

# exibe frequências acumuladas
# print(fac)