import random

alunos = ['Guilherme', 'Ricardo', 'Rodrigo', 'Danieli', 'Ana', 'Arthur', 'Rogério', 'Matheus', 'Raissa', 'Pedro', 'Carlos', 'Vitor', 'Felipe', 'Andrew', 'Guilherme C.', 'Caio', 'Miguel', 'Geovanna', 'Renan', 'Vinicius']

# amostragem aleatória simples
amostra = random.sample(alunos, 3)
print(amostra)

# amostra fixa (reprodutibilidade)
random.seed(20)
amostraFixa = random.sample(alunos, 3)
print(amostraFixa)