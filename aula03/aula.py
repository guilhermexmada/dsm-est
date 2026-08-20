# população = conjunto completo de elementos com a característica que se deseja estudar (pessoas, professores, alunos, vendas, produtos, etc)
populacao = 100
# amostra = parte da população selecionada para análise, de modo a representar a população
amostra = populacao * 0.01

print(f'Dentre uma população de {populacao} foi selecionada uma amostra de {amostra}')

# censo = análise de toda a população (mais caro, demorado e difícil de ser realizado)
qtdPerguntas = 2 
censo = qtdPerguntas * populacao

print(f'Um censo de 2 questões realizado em uma população de {populacao} contou com um total de {censo} perguntas realizadas')

# populações comuns em ciências de dados: clientes, transações, acessos, pedidos, sensores, usuários, eventos -> define sobre quem ou o que queremos tirar conclusões

# parâmetro = dado/medida calculada usando toda a população
# estatística = dado/medida calculada usando uma amostra 

popIdades = [10, 20, 30, 40, 50]

parametro = (popIdades[0] + popIdades[1] + popIdades[2] + popIdades[3] + popIdades[4]) / len(popIdades)

estatistica = (popIdades[1] + popIdades[3]) / 2

# uma amostra pode representar uma população que está distribuída de maneira adequada, tudo depende da qualidade da amostra

# viés de seleção = escolha enviesada da amostra conclui uma análise que não representa adequadamente a população (processo de coleta de amostra inadequado conduz a dados que fogem da realidade)

# amostragem aleatória simples = todos os elementos da população possuem a mesma chance de serem escolhidos

# amostragem sistemática = elementos selecionados seguindo um intervalo = (pop / am)

# amostragem estratificada = população dividida em grupos chamados "estratos", selecionamos indivíduos (%) de cada grupo (ex: 5% dos alunos de cada turma de DSM da FATEC)

# amostragem por conglomerados = população dividida em grupos naturais / grupos inteiros / "conglomerados" (ex: escolhidas 10 escolas em uma rede com 100 escolas)

# a média da amostra não precisa ser igual à média da população, pois é uma parte do todo, incluindo erro amostral

# erro amostral = diferença entre medida da população e estimativa da amostra (não necessáriamente é um erro processual, mas uma consequência estatística)