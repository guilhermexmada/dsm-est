import pandas as pd 

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduarda', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia', 'Lucas', 'Marina'],
    'Nota': [8,7,9,6,10,8,7,9,5,8,6,10]
}

alunos = pd.DataFrame(dados)

# verificar tamanho da população
print(f'Tamanho da população: {alunos.shape[0]}')

# calcular média da população
mediaPop = alunos['Nota'].mean()
print(f'Média de notas da população: {mediaPop}')

for size in [5, 8]:
    # retirar amostra de 5 e 8 alunos
    amostra = alunos.sample(n=size)
    print(f'Amostra: \n {amostra}')

    # calcular a média da amostra
    mediaAm = amostra['Nota'].mean()
    print(f'Média de notas da amostra: {mediaAm}')

    # comparar médias
    erroAmostral = mediaPop - mediaAm
    print(f'Erro amostral: {erroAmostral:.2f}')