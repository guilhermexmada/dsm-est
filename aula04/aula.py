# considerando uma amostra muito grande, como organizar e resumir os dados de uma amostra?

# dados brutos são dados desorganizados
dadosBrutos = [7,8,5,9,6,7,4,8,7,6,9,4,5,7,2,4,6,8,0,1,2,3] # população
dadosAlvo = [7,8,9] # amostra

freqAbsoluta = 0
freqAcumulada = 0

for i in dadosAlvo:
    for j in dadosBrutos:
        if i == j:
            freqAbsoluta = freqAbsoluta + 1
    # frequência absoluta é a quantidade de vezes que o valor ocorre em um conjunto de dados
    print(f'Frequência absoluta de {j}: {freqAbsoluta}')
    # frequência relativa é a proporção de cada valor em relação ao total ( fr = fa / n) onde n = quantidade total de dados
    print(f'Frequência relativa de {j}: {freqAbsoluta/len(dadosBrutos):.2f}')
    # frequência acumulada soma profressivamente as frequências anteriores (dos outros dados)
    freqAcumulada = freqAcumulada + freqAbsoluta
    print(f'Frequência acumulada de {j}: {freqAcumulada}')
    print('--------------------')
    freqAbsoluta = 0
