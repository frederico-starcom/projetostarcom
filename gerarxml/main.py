import xml.etree.cElementTree as et
from random import randint

__version__ = '1.0'
__author__ = 'Frederico Gustavo Magalhães'

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

tamdesenho = 11
tamvalor = 10

root = et.Element('NFeB2BFin')
doc = et.SubElement(root, 'iCab')

et.SubElement(doc, 'versao').text = '1'
et.SubElement(doc, 'fMensg').text = '9'
et.SubElement(doc, 'nDoc')
et.SubElement(doc, 'dEmiDoc')
et.SubElement(doc, 'tpNF').text = '241'

nota = input('Número da nota fiscal. ')
et.SubElement(doc, 'nNF').text = nota

et.SubElement(doc, 'serie').text = '1'
et.SubElement(doc, 'dEmi').text = input('Data da emissão da nota fiscal. ')
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

# Realiza a inclusão de novos desenhos ao XML Logístico
while True:
    produto = et.SubElement(doc, 'prod')

    linha = GeraNumLinha()
    et.SubElement(produto, 'nLin').text = linha
        
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
    et.SubElement(produto, 'qPed').text = input('Informe a quantidade solicitado do desenho. ')
    et.SubElement(produto, 'unidMedProd').text = 'EA'
                
    NFref = et.SubElement(produto, 'NFref')
    infItensComp = et.SubElement(NFref, 'infItensComp')
    et.SubElement(infItensComp, 'cCAdicProdClie').text = desenho
                
    automotivo = et.SubElement(produto, 'automotivo')
    et.SubElement(automotivo, 'tpFornec').text = 'P'
    infCompCarg = et.SubElement(automotivo, 'infCompCarg')
    et.SubElement(infCompCarg, 'dEmbContida')
                
    # Realiza a inclusão de novos progressivos referentes ao desenho cadastrado ao XML Logístico
    while True:
        ReqIntern = et.SubElement(produto, 'ReqIntern')
        et.SubElement(ReqIntern, 'tpPedCham').text = '001'
        et.SubElement(ReqIntern, 'nPedCham').text = input('Informe o número do progressivo. ')
        et.SubElement(ReqIntern, 'dhPedCham').text = input('Informe a data e a hora com o seguinte formato AAAA-MM-DDTHH:MM:SS: ')
        et.SubElement(ReqIntern, 'qPedCham').text = '1'
        et.SubElement(ReqIntern, 'qEmbalag').text = '10'
                    
        sair = input(f'Deseja continuar cadastrando os PROGRESSIVOS para o desenho "{desenho}"? "S" para SAIR e "C" para CONTINUAR ').upper()
                    
        if sair == 'S':
            break
                
    infoTemp = et.SubElement(produto, 'infoTemp')
    
    sair = input(f'Deseja continuar cadastrando os DESENHOS para o XML Logístico {nota}? "S" para SAIR e "C" para CONTINUAR ').upper()
                
    if sair == 'S':
        break

tree = et.ElementTree(root)
tree.write('filename.xml')
