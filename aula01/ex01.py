import pandas as pd

dados = {
    "Nome" : ["João", "Maria", "Pedro", "Ana"],
    "Idade" : [18, 20, 19, 22]
}

# monta dataframe
df = pd.DataFrame(dados)

# exibe 
print(df.head())

# conta registros
print(len(df))

# visualiza informações
# print(df.describe())