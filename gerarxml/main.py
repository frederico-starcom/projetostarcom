#! /usr/bin/python3
# coding: utf-8


import xml.etree.cElementTree as et

from datetime import datetime

__version__ = '1.1'
__author__ = 'Frederico Gustavo Magalhães'


# Verifica se o tamanho do registro é igual ao tamanho infomado na função
def ValidaTamanho(value, size):
    line = ''
    if len(value) < size:
        newline = line + value
        while len(newline) != size:
            line += '0'
            newline = line + value
        return newline
    else:
        return value



root = et.Element('NFeB2BFin')
doc = et.SubElement(root, 'iCab')

et.SubElement(doc, 'versao').text = '1'
et.SubElement(doc, 'fMensg').text = '9'
et.SubElement(doc, 'nDoc')
et.SubElement(doc, 'dEmiDoc')
et.SubElement(doc, 'tpNF').text = '241'

invoice_number = input('Número da nota fiscal. ')
et.SubElement(doc, 'nNF').text = invoice_number

et.SubElement(doc, 'serie').text = '1'

data_emissao = input('Data da emissão da nota fiscal(YYYY-MM-DD) ')
et.SubElement(doc, 'dEmi').text = data_emissao

et.SubElement(doc, 'chNFe').text = input('Informe a chave da nota fiscal. ')

part = et.SubElement(doc, 'partes')
emit = et.SubElement(part, 'emit')
et.SubElement(emit, 'tpEmit').text = '001'
et.SubElement(emit, 'cEmit').text = '18202870000109'
embarque = et.SubElement(part, 'embarque')
et.SubElement(embarque, 'tpEmbarque').text = '001'
et.SubElement(embarque, 'cEmbarque').text = '18202870000109'
entrega = et.SubElement(part, 'entrega')
et.SubElement(entrega, 'tpEntrega').text = '001'
et.SubElement(entrega, 'cEntrega').text = '16701716000156'
comprador = et.SubElement(part, 'comprador')
et.SubElement(comprador, 'tpComprador').text = '001'
et.SubElement(comprador, 'cComprador').text = '16701716000156'
fabricante = et.SubElement(part, 'fabricante')
et.SubElement(fabricante, 'tpFabricante').text = '001'
et.SubElement(fabricante, 'cFabricante').text = '16701716000156'

transp = et.SubElement(doc, 'transp')
et.SubElement(transp, 'codEntrega').text = 'CIF'
et.SubElement(transp, 'motorista')
et.SubElement(transp, 'tpTrans')
et.SubElement(transp, 'transportadora')

# Declaração das variáveis
count_progressivo = 0
tamdesenho = 11
tamvalor = 10
tamprogres = 6

# Realiza a inclusão de novos desenhos ao XML Logístico
while True:
    count_progressivo += 1

    produto = et.SubElement(doc, 'prod')

    count_progressivo_str = str(count_progressivo)
    linha = ValidaTamanho(count_progressivo_str, tamprogres)
    et.SubElement(produto, 'nLin').text = str(linha)

    numdesenho = input('Digite o número do desenho. ')

    # Valida a qtde de caracteres digitados no campo DESENHO
    desenho = ValidaTamanho(numdesenho, tamdesenho)

    et.SubElement(produto, 'cAdicProdClie').text = desenho
    et.SubElement(produto, 'vProd')

    ValorTotalDesenho = input('Informe o valor total do desenho. ').replace(',', '').replace('.', '')

    # Valida a qtde de caracteres digitados no campo ValorTotalDesenho
    valor = ValidaTamanho(ValorTotalDesenho, tamvalor)

    et.SubElement(produto, 'vLiqTot').text = valor

    ValorUnitDesenho = input('Informe o valor uniário do desenho. ').replace(',', '').replace('.', '')

    # Valida a qtde de caracteres digitados no campo ValorUnitDesenho
    valorunit = ValidaTamanho(ValorUnitDesenho, tamvalor)

    et.SubElement(produto, 'vLiqUni').text = valorunit
    et.SubElement(produto, 'vUnCom').text = '000000000000000.00'
    et.SubElement(produto, 'iPesoB').text = '000000000000000.400'
    et.SubElement(produto, 'iPesoL').text = '000000000000000.400'

    qtde_progressivo = int(input('Informe a quantidade solicitado do desenho. '))
    et.SubElement(produto, 'qPed').text = str(qtde_progressivo)

    et.SubElement(produto, 'unidMedProd').text = 'EA'

    NFref = et.SubElement(produto, 'NFref')
    infItensComp = et.SubElement(NFref, 'infItensComp')
    et.SubElement(infItensComp, 'cCAdicProdClie').text = desenho

    automotivo = et.SubElement(produto, 'automotivo')
    et.SubElement(automotivo, 'tpFornec').text = 'P'
    infCompCarg = et.SubElement(automotivo, 'infCompCarg')
    et.SubElement(infCompCarg, 'dEmbContida')

    # Realiza a inclusão de novos progressivos referentes ao desenho cadastrado ao XML Logístico
    count = 0
    while qtde_progressivo > count:
        ReqIntern = et.SubElement(produto, 'ReqIntern')
        et.SubElement(ReqIntern, 'tpPedCham').text = '001'
        et.SubElement(ReqIntern, 'nPedCham').text = input(f'Informe o número do {count + 1}º progressivo: ')

        data_formatada = data_emissao + 'T00:00:00'
        et.SubElement(ReqIntern, 'dhPedCham').text = str(data_formatada)

        et.SubElement(ReqIntern, 'qPedCham').text = '1'
        et.SubElement(ReqIntern, 'qEmbalag').text = '10'

        count += 1

    infoTemp = et.SubElement(produto, 'infoTemp')

    sair = input(
        f'Deseja continuar cadastrando os DESENHOS para o XML Logístico {invoice_number}? "S" para SIM e "N" para NÃO ').upper()

    if sair == 'N':
        break

tree = et.ElementTree(root)

try:
    date_xml = datetime.now()
    date_string = date_xml.strftime('%Y%m%d%H%M%S')
    file_name = '000033228_0000'
    complement = '_001_'
    tree.write(f'{file_name}{invoice_number}{complement}{date_string}.xml')
    print('Aquivo criado com sucesso!')
    del count_progressivo
except:
    print('Erro ao criar o arquivo!')
