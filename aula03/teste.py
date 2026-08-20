import random
import pandas as pd
import matplotlib.pyplot as plt

caracQual = {
    pele: ['branco', 'negro', 'pardo', 'amarelo', 'vermelho'],
    sexo: ['feminino', 'masculino'],
    mao: ['destro', 'canhoto', 'ambidestro'],
    corPredileta: ['azul', 'amarelo', 'vermelho', 'verde', 'marrom', 'roxo', 'rosa', 'cinza', 'preto', 'laranja', 'branco', 'nenhuma']
    petFavorito: ['cão', 'gato', 'passarinho', 'ramster', 'jabuti', 'cobra', 'peixe', 'galinha', 'nenhum'],
    estado: ['SP', 'MG', 'ES', 'RJ', 'MS', 'MT', 'GO', 'RS', 'PR', 'SC', 'AC', 'AM', 'RO', 'RD', 'PA', 'AP', 'TO', 'MA', 'PI', 'BA', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE']
}

caracQuant = {
    idade: random.radint(18, 80),
    altura: random.uniform(0.5, 2.5)
} 