"""
Arquivo que armazena as funções de validação e criação do XML.
@Autor: Frederico Gustavo Magalhães
@Data: 2021-04-15
"""

import xml.etree.cElementTree as et

from datetime import datetime
from random import randint

# Função cria o número da linha de forma randômica
def GeraNumLinha():
    linha = str(randint(0, 999999))
    tamanho = 6
    
    return ValidaTamanho(linha, tamanho)


# Verifica se o tamanho do registro é igual ao tamanho infomado na função
def ValidaTamanho(valor, tamanho):
    linhazero = ''
    
    if len(valor) < tamanho:
        novalinha = linhazero + valor
        while len(novalinha) != tamanho:
            linhazero += '0'
            novalinha = linhazero + valor
        return novalinha
    else:
        return (valor)


# Função cria o arquivo XML
def GeraXML(document):
    tree = et.ElementTree(document)
    date = datetime.now()
    date_string = date.strftime('%Y-%m-%d-%H:%M:%S')
    
    try:
        tree.write(f'{date_string}.xml')
        print('Arquivo criado com sucesso.')
    except:
        print('Não foi possível criar o arquivo XML.')
