# import xml.etree.cElementTree as et

# from datetime import datetime

# from django.db import models


# # Create your models here.
# class Xml(models.Model):
#     date_create = models.CharField(max_length=10, verbose_name="Data de emissão")
#     invoice_number = models.CharField(max_length=7, verbose_name="Número da nota")
#     invoice_key = models.CharField(max_length=44, verbose_name="Chave da nota")
#     part_number = models.CharField(max_length=12, verbose_name="Número do desenho")
#     value_total_drawing = models.CharField(max_length=10, verbose_name="Valor total do desenho")
#     value_unit_drawing = models.CharField(max_length=10, verbose_name="Valor unitário do desenho")
#     amount_drawing = models.CharField(max_length=10, verbose_name="Quantidade solicitada")
#     number_progressive = models.CharField(max_length=5, verbose_name="Número do progressivo")
#     date_create_progressive = models.CharField(max_length=10, verbose_name="Data de criação")

#     # Verifica se o tamanho do registro é igual ao tamanho infomado na função
#     def ValidateSize(value, size):
#         line = ''
#         if len(value) < size:
#             newline = line + value
#             while len(newline) != size:
#                 line += '0'
#                 newline = line + value
#             return newline
#         else:
#             return value

#     # Função responsável por criar o arquivo XML
#     def CreateXML(self, root):
#         tree = et.ElementTree(root)

#         try:
#             date_xml = datetime.now()
#             date_string = date_xml.strftime('%Y%m%d%H%M%S')
#             file_name = '000033228_0000'
#             complement = '_001_'
#             # tree.write(f'{file_name}{nota}{complement}{date_string}.xml')
#             print('Aquivo criado com sucesso!')
#         except:
#             print('Erro ao criar o arquivo!')
    
#     def __str__(self):
#         return self.invoice_number

