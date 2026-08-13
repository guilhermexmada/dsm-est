import pandas as pd

dados = {
    'Nome': [
        'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo',
        'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
        'Lucas', 'Mariana', 'Nathan', 'Olivia', 'Pedro',
        'Rafael', 'Sofia', 'Thiago', 'Valentina', 'Yuri'
    ],
    'Idade': [
        18, 19, 17, 20, 18,
        21, 19, 17, 20, 18,
        22, 19, 18, 21, 20,
        19, 17, 22, 18, 20
    ],
    'Nota': [
        8.5, 7.8, 9.2, 6.5, 8.9,
        7.4, 9.5, 8.1, 6.9, 9.0,
        7.7, 8.8, 9.3, 7.1, 8.4,
        6.8, 9.7, 8.6, 7.9, 9.1
    ]
}

df = pd.DataFrame(dados)

print(df) # exibe dataframe

print(df.head()) # exibe as primeiras linhas com head()

print(df.describe()) # exibe dados estatísticos relevantes com describe()

print(df.info()) # exibe informações gerais com info()