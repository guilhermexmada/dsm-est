import pandas as pd

dados = {
    "Nome": [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Kaique", "Larissa", "Marcos", "Natália", "Otávio",
        "Patrícia", "Rafael", "Sabrina", "Thiago", "Vanessa",
        "Wesley", "Yasmin", "André", "Beatriz", "Caio",
        "Débora", "Felipe", "Giovana", "Henrique", "Isabela"
    ],
    "Idade": [
        18, 21, 19, 25, 22,
        20, 24, 18, 27, 23,
        19, 26, 21, 20, 28,
        22, 24, 19, 30, 21,
        23, 18, 26, 25, 20,
        22, 27, 19, 24, 21
    ],
    "Nota": [
        8.5, 7.2, 9.1, 6.8, 8.7,
        7.9, 9.5, 6.4, 8.2, 7.6,
        9.0, 8.8, 7.3, 9.4, 6.9,
        8.1, 7.7, 9.2, 6.5, 8.9,
        7.1, 9.6, 8.4, 7.8, 9.3,
        6.7, 8.6, 7.5, 9.7, 8.0
    ]
}

alunos = pd.DataFrame(dados)

print(f'\n=== Analisando população de {len(alunos)} alunos ===\n')

mediaNotaPop = alunos['Nota'].mean()
mediaIdadePop = alunos['Idade'].mean()

print(f'Média das notas da população: {mediaNotaPop:.2f}')
print(f'Média das idades da população: {mediaIdadePop:.2f}')

for size in [5, 10]:
    print(f'\n=== Analisando amostra de {size} alunos ===\n')
    amostra = alunos.sample(n=size)
    mediaNotaAm = amostra['Nota'].mean()
    mediaIdadeAm = amostra['Idade'].mean()
    erroAmostralNota = mediaNotaPop - mediaNotaAm
    erroAmostralIdade = mediaIdadePop - mediaIdadeAm
    print(f'Média das notas da amostra: {mediaNotaAm:.2f}')
    print(f'Erro amostral: {erroAmostralNota:.2f}')
    print(f'Média das idades da amostra: {mediaIdadeAm:.2f}')
    print(f'Erro amostral: {erroAmostralIdade:.2f}')