'''
from random import randint

def GeraNumLinha():
    linha = randint(0, 999999)
    linha = str(linha)
    #count = 0
    linhazero = novalinha = ''

    if len(linha) < 6:
        novalinha = linhazero + linha
        while len(novalinha) != 6:
            linhazero += '0'
            novalinha = linhazero + linha
            #count += 1
        return novalinha
    else:
        return (linha)


print(GeraNumLinha())

import datetime

data_usuario = '2015-04-25'
data_formatada = datetime.datetime.strptime(data_usuario,'%Y-%m-%d')
print(data_formatada)

# tm_hour=14, tm_min=17, tm_sec=2,
'''

while True:
    print('Estou no PRIMEIRO WHILE!')
    
    for n in range(1, 10):
        linha = n

        while True:
            print('Estou no SEGUNDO WHILE!')
            print(linha)

            op2 = input('Deseja continuar "S/N" ').upper()

            if op2 == 'N':
                break
    
    op = input('Deseja continuar "S/N" ').upper()
    if op == 'N':
        break
    
    