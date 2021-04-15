import xml.etree.cElementTree as et
import sys, os
from random import randint
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton

# Classe responsável por montar a tela de cadastro
class Form(QDialog):

    # função de construção da classe que monta o formulário de cadastro
    def __init__(self, parents=None):
        super(self, Form).__init__(parent)

        self.setWindowTitle('Starcom')
        self.edit = QLineEdit('Data da emissão')

# Classe para montagem do XML
class Xml():

    # função de construção da classe Xml
    def __init__(self):
        super(self, Xml).__init__()

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

    # Função utilizada para gerar os XML logísticos
    def GeraXML(document):
        tree = et.ElementTree(document)
        try:
            tree.write('filename.xml')
            print('Arquivo criado com sucesso.')
        except:
            print('Erro na criação do arquivo.')


if __name__ == '__main':

    app = QApplication(sys.argv)
    form = Form()
    form.show()

    sys.exit(app.exec_())
