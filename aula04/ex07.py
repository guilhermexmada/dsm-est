import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'id': list(range(1, 101)),

    'idade': [
        22, 25, 31, 19, 28, 35, 42, 24, 30, 27,
        21, 33, 45, 26, 38, 29, 23, 41, 34, 20,
        32, 36, 48, 25, 39, 27, 44, 31, 22, 37,
        29, 40, 24, 35, 50, 28, 33, 21, 46, 30,
        26, 43, 34, 19, 38, 27, 49, 32, 23, 36,
        41, 25, 30, 47, 28, 35, 22, 39, 31, 24,
        45, 29, 37, 20, 42, 33, 26, 48, 34, 21,
        38, 27, 44, 32, 23, 40, 30, 36, 25, 49,
        28, 43, 31, 19, 35, 46, 24, 39, 33, 22,
        41, 29, 37, 26, 45, 32, 20, 34, 28, 50
    ],

    'sistema_operacional': [
        'Windows', 'Linux', 'Android', 'Windows', 'macOS',
        'Android', 'Windows', 'iOS', 'Linux', 'Windows',
        'macOS', 'Android', 'Windows', 'Linux', 'iOS',
        'Windows', 'Android', 'macOS', 'Linux', 'Windows',
        'Android', 'Windows', 'Linux', 'iOS', 'macOS',
        'Windows', 'Android', 'Linux', 'Windows', 'macOS',
        'iOS', 'Windows', 'Linux', 'Android', 'Windows',
        'macOS', 'Android', 'Linux', 'Windows', 'iOS',
        'Windows', 'Android', 'macOS', 'Linux', 'Windows',
        'iOS', 'Android', 'Windows', 'Linux', 'macOS',
        'Windows', 'Linux', 'Android', 'iOS', 'Windows',
        'macOS', 'Windows', 'Android', 'Linux', 'Windows',
        'iOS', 'Android', 'Windows', 'macOS', 'Linux',
        'Windows', 'Android', 'Linux', 'iOS', 'Windows',
        'macOS', 'Windows', 'Android', 'Linux', 'Windows',
        'iOS', 'Windows', 'macOS', 'Android', 'Linux',
        'Windows', 'Android', 'iOS', 'Linux', 'macOS',
        'Windows', 'Android', 'Linux', 'Windows', 'iOS',
        'macOS', 'Windows', 'Android', 'Linux', 'Windows',
        'iOS', 'macOS', 'Android', 'Windows', 'Linux'
    ],

    'linguagem_preferida': [
        'Python', 'JavaScript', 'Java', 'Python', 'TypeScript',
        'Java', 'C#', 'Python', 'PHP', 'JavaScript',
        'C++', 'Python', 'Java', 'Go', 'TypeScript',
        'Python', 'JavaScript', 'Ruby', 'C#', 'Java',
        'Python', 'PHP', 'JavaScript', 'Rust', 'Python',
        'Java', 'C++', 'TypeScript', 'Python', 'Go',
        'JavaScript', 'Python', 'C#', 'Java', 'PHP',
        'TypeScript', 'Python', 'Ruby', 'Java', 'C++',
        'Python', 'JavaScript', 'Go', 'PHP', 'Rust',
        'Java', 'Python', 'C#', 'TypeScript', 'JavaScript',
        'Python', 'Java', 'PHP', 'C++', 'Python',
        'Ruby', 'JavaScript', 'TypeScript', 'Python', 'C#',
        'Go', 'Python', 'Java', 'Rust', 'JavaScript',
        'PHP', 'Python', 'C++', 'TypeScript', 'Java',
        'Python', 'Ruby', 'JavaScript', 'C#', 'Go',
        'Python', 'Java', 'PHP', 'TypeScript', 'Python',
        'C++', 'JavaScript', 'Rust', 'Python', 'Java',
        'Go', 'C#', 'Python', 'PHP', 'JavaScript',
        'TypeScript', 'Python', 'Ruby', 'Java', 'C++',
        'Python', 'JavaScript', 'C#', 'Go', 'Python'
    ],

    'tempo_uso_diario': [
        3.5, 5.2, 7.0, 2.5, 6.0, 8.5, 4.0, 5.5, 3.0, 6.5,
        2.0, 7.5, 9.0, 4.5, 6.0, 3.5, 5.0, 8.0, 4.0, 2.5,
        6.5, 7.0, 9.5, 3.0, 5.5, 4.0, 8.5, 6.0, 2.5, 7.5,
        5.0, 8.0, 3.5, 6.5, 10.0, 4.5, 7.0, 2.0, 9.0, 5.5,
        3.0, 8.5, 6.0, 2.5, 7.5, 4.0, 9.5, 5.0, 3.5, 8.0,
        6.5, 4.0, 5.5, 9.0, 3.0, 7.0, 2.5, 8.5, 5.0, 4.5,
        9.5, 3.5, 7.5, 2.0, 8.0, 6.0, 4.0, 10.5, 5.5, 3.0,
        7.0, 4.5, 9.0, 5.0, 2.5, 8.5, 6.5, 7.5, 3.5, 9.5,
        4.0, 8.0, 5.5, 2.0, 7.0, 9.0, 3.0, 6.5, 5.0, 4.5,
        8.5, 3.5, 7.5, 4.0, 9.5, 6.0, 2.5, 8.0, 5.5, 10.0
    ]
}

df = pd.DataFrame(dados)

# para cada coluna do dataframe
for coluna in df.columns:
    print(f'=== Análise Estatística | {coluna} ===')
    # monta uma Series
    series = df[coluna]
    # calcula frequências
    frq_abs = series.value_counts().sort_index()
    frq_rel = frq_abs / len(series)
    frq_acm = frq_abs.cumsum()
    frq_max = frq_abs.max()
    val_frq_max = frq_abs.idxmax()
    frequencias = {
        'Freq. Absoluta': frq_abs,
        'Freq. Relativa': frq_rel,
        'Freq. Acumulada': frq_acm,
    }
    print(f'Freq. Máxima: {frq_max}')
    print(f'Valor com freq. máxima: {val_frq_max}')
    tabela = pd.DataFrame(frequencias)
    print(tabela)
    # monta gráficos 
    frq_abs.plot(kind='bar')
    plt.title(f'Frequências de {coluna}')
    plt.xlabel('Valor')
    plt.ylabel('Categoria')
    plt.show()
    frq_abs.plot(kind='pie')
    plt.title(f'Distribuição de {coluna}')
    plt.xlabel('Valor')
    plt.ylabel('Categoria')
    plt.show()
    plt.hist(series, bins=5)
    plt.xlabel(f'{coluna}')
    plt.ylabel("Frequência")
    plt.title(f'Frequências de {coluna}')
    plt.show()
    if series.dtype in ['int64', 'float64']:
        plt.boxplot(series)
        plt.ylabel(f'{coluna}')
        plt.title(f'Distribuição de {coluna}')
        plt.show()

