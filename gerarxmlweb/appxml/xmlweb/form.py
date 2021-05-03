from django import forms
from datetime import datetime
import xml.etree.ElementTree as ET

class XmlForm(forms.Form):
    date_create = forms.CharField(max_length=10, label="Data de emissão")
    invoice_number = forms.CharField(max_length=7, label="Número da nota")
    invoice_key = forms.CharField(max_length=44, label="Chave da nota")
    part_number = forms.CharField(max_length=12, label="Número do desenho")
    value_total_drawing = forms.CharField(max_length=10, label="Valor total do desenho")
    value_unit_drawing = forms.CharField(max_length=10, label="Valor unitário do desenho")
    amount_drawing = forms.CharField(max_length=10, label="Quantidade solicitada")
    number_progressive = forms.CharField(max_length=5, label="Número do progressivo")
    date_create_progressive = forms.CharField(max_length=10, label="Data de criação")

    # Verifica se o tamanho do registro é igual ao tamanho infomado na função
    def ValidateSize(self, value, size):
        line = ''
        if len(value) < size:
            newline = line + value
            while len(newline) != size:
                line += '0'
                newline = line + value
            return newline
        else:
            return value

    # Função responsável por criar o arquivo XML
    def CreateXML(self, root):
        tree = ET.ElementTree(root)

        try:
            date_xml = datetime.now()
            date_string = date_xml.strftime('%Y%m%d%H%M%S')
            file_name = '000033228_0000'
            complement = '_001_'
            tree.write(f'{file_name}{invoice_number}{complement}{date_string}.xml')
            print('Aquivo criado com sucesso!')
        except:
            print('Erro ao criar o arquivo!')
