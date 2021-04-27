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
'''
import datetime

data_usuario = '2015-04-25'
data_formatada = datetime.datetime.strptime(data_usuario,'%Y-%m-%d')
print(data_formatada)

# tm_hour=14, tm_min=17, tm_sec=2,