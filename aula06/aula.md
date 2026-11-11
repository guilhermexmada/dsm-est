# Estatística - Aula 06

## Medidas de tendência central

Considere uma API com as seguintes medições dos tempos de resposta para diferentes requisições:

```
req01 - 100ms
req02   90ms
req03 - 105ms
req04 - 120ms
req05 - 115ms
```

Se alguém te perguntar "Qual o tempo de resposta típico desse serviço?", como responder?

Um relatório com todos os dados crus não é nada prática. Precisamos de um indicador representativo, que busca estar no "centro" da distribuição dos valores.

Uma medida de **tendência central** busca representar um conjunto de dados através de um único valor central.

- Média (x̄) : a soma de todos os valores dividida pelo total de dados;
- Mediana (Md) : o valor na posição central quando os dados estão ordenados;
- Moda (Mo) : o valor que mais aparece no conjunto de dados;

### Média Aritmética

A média aritmética é a medida central mais intuitiva. Ela é considerada o "ponto de equilíbrio físico" entre os dados.

```
# fórmula matemática

x̄ = (x₁ + x₂ + x₃ + xₙ) / n 

x̄ = média aritmética; xᵢ = valor individual; n = total de dados

# exemplo 

notas: { 10, 8, 7.5}

média = (10 + 8 + 7.5) / 3 = 8.5
```

Para calcular média em python puro:

```
# Exemplo de cálculo em Python puro
notas = [8, 7, 9, 6, 10]

# Somando e dividindo manualmente
soma = sum(notas)

quantidade = len(notas)

media = soma / quantidade

print(media) # Saída esperada: 8.0
```

Utilizando a biblioteca Pandas, use o método interno `mean()` para manipular `Series`.

```
import pandas as pd

# Criando uma Series a partir da lista

notas = pd.Series([8, 7, 9, 6, 10])

# Calculando a média de forma direta

media = notas.mean()

print(media) # Saída esperada: 8.0
```

Também existe o método `describe()`, cuja análise estatística traz vários dados, incluindo `mean`.

```
import pandas as pd

notas = pd.Series([8, 7, 9, 6, 10])

# Exibindo o resumo estatístico completo

print(notas.describe())
```

No entanto, a média aritmética apresenta um problema importante.

Considere o conjunto {10, 10, 10, 10, 100} - a média exata desses dados é 28. Mas 28 representa bem o centro desse conjunto?

Observe que um único valor 100 é muito discrepante em relação aos outros dados, que são todos 10. **Valores discrepantes podem distorcer completamente o comportamento da média de um conjunto**. Isso porque eles "puxam" a média para cima ou para baixo, diminuindo a representatividade da medida.

Esse valor discrepante/extremo é conhecido como *Outlier*.

### Mediana

É o valor que ocupa a posição central quando os dados estão ordenados, seja em ordem crescente ou decrescente. A mediana "divide o conjunto ao meio", com 50% dos dados acima e 50% abaixo.

```
# conjunto ordenado

{3, 5, 7, 9, 11}

{3, 5, [7], 9, 11}

# mediana = 7
```

E quando a quantidade dos dados é ímpar? Você tira a média dos 2 valores no centro!

```
# conjunto ordenado

{10, 20, 30, 40}

{10, [20, 30], 40}

# mediana = (20 + 30) / 2

# mediana = 25 
```

Utilizando a biblioteca Pandas, calcule a mediana usando o método interno `median()`. Ele serve para `Series` e `Dataframes`, e cuida sozinho da ordenação dos dados e de conjuntos com total ímpar/par.

```
import pandas as pd

# Definindo o conjunto de notas
notas = pd.Series([8, 7, 9, 6, 10])

# Calculando a mediana diretamente
mediana = notas.median()

print(mediana) # Saída esperada: 8.0
```

Comparando média e mediana, podemos descobrir uma diferença de "sensibilidade" entre as duas medidas centrais: **Outliers afetam drasticamente médias, mas não tem quase nenhuma importância ao calcular mediana**. Isso porque a média usa todos os valores, e a mediana não - ela só "olha" pra 1 valor.

Portanto, a mediana é bem mais eficiente contra assimetrias e Outliers, pois representa esses conjuntos de dados com mais fidelidade que a média.

### Moda

Medida de tendência central que indica o valor mais frequente em um determinado conjunto.

O valor que "está na moda" é simplesmente o que mais se repete.

```
# exemplo
[2, 3, 3, 4, 5]

valor | ocorrências
2 | x1
3 | x2
4 | x1
5 | x1

# moda = 3
```

Usando a biblioteca Pandas, calcule a moda em python pelo método interno `mode()`, que serve para `Series` e `Dataframes`. A saída dele é sempre uma `Series` e não um único número - isso ocorre porque um conjunto de dados pode ter mais de uma moda simultaneamente...

```
import pandas as pd

# Definindo o conjunto de dados
dados = pd.Series([2, 3, 3, 4, 5])

# Calculando a moda
moda = dados.mode()

print(moda)

# Saída esperada:
# 0 3
# dtype: int64
```

**Conjunto bimodal** é um conjunto de dados no qual 2 ou mais valores empatam em frequência máxima, constituindo 2 ou mais modas para o mesmo conjunto.

*(Obs.: unimodal = 1 moda, bimodal = 2 modas, multimodal = 3+ modas)*

```
# exemplo
[1, 1, 2, 2, 3] -> conjunto bimodal

valores | ocorrências
1 | x2
2 | x2
3 | x1

# moda = {1, 2}
```

A moda é interessante para analisar dados **não categóricos (não numéricos)**: diferente da média e mediana que exigem operações ou ordenação, a moda conta ocorrências. 

Imagine um conjunto de palavras. Não há como calcular a média delas, e a ordenação das mesmas pode ser mais demorada (ordem alfabética). É bem mais simples contar quantas vezes cada uma aparece.

```
# exemplo
['Windows', 'Windows', 'Linux', 'macOS', 'Linux', 'Windows']

valores | ocorrências
'Windows' | x3
'Linux' | x2
'macOS' | x1

# moda = 'Windows'
```

Como a moda usa os valores que mais aparecem e, por definição, Outliers são valores menos frequentes e mais distantes do centro do conjunto, podemos dizer que a moda possui uma sensibilidade nula à Outliers.

### Média Ponderada

Na média ponderada, a importância (peso) dos valores pode variar. Nesse caso, cada elemento é multiplicado por seu respectivo peso, e o resultado acumulado é dividido pela soma dos pesos.

```
# fórmula matemática

x̄ₚ = (Σ xᵢ · wᵢ) / Σ wᵢ

# exemplo
avaliação | nota | peso
prova | 8.0 | 3.0
trabalho | 7.0 | 2.0
projeto | 10.0 | 5.0

media_ponderada = (8*3) + (7*2) + (10*5) / (3+2+5) = 88/10 = 8.8
```

Em python, use a função `zip()` para unir uma lista de elementos com uma lista de pesos. Aplicando a multiplicação e a soma, conseguimos calcular a média ponderada sem depender de pacotes externos.

```
# Exemplo em Python estruturado
notas = [8, 7, 10]
pesos = [3, 2, 5]

# Utilizando compreensão de lista e zip()
numerador = sum(
 nota * peso
 for nota, peso in zip(notas, pesos)
)

denominador = sum(pesos)
media_ponderada = numerador / denominador

print(media_pond) # Saída esperada: 8.8
```

Já a biblioteca NumPy oferece um método `average()` específico para média ponderada. Ele usa o parâmetro `weights` para associar uma lista de valores a uma lista de pesos. É considerado um padrão para ciência de dados, *machine learning* e processamento de matrizes multidimensionais.

```
import numpy as np

notas = [8, 7, 10]
pesos = [3, 2, 5]

# Utilizando a função np.average()
media_pond = np.average(
 notas,
 weights=pesos
)

print(media_pond) # Saída esperada: 8.8
```