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