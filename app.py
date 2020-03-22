import textract
import json
import csv

# Texto extraido con UTF-8 para que acepte acentos
text = textract.process('pdf/Punto_14.pdf', method='pdfminer', encoding='utf-8')

# Decodificar el texto
text_to_string = text.decode('utf-8')
k   =   len(text_to_string)
for j in range(0,k):
    text_data= text_to_string[j].split('\n')
    print(text_data)
