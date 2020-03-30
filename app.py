import PyPDF2 as pdf
import numpy
import pandas

pdf_file = open('pdf/Punto_14.pdf', 'rb')

read_pdf = pdf.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()

for page_number in range(number_of_pages):   # use xrange in Py2

        page = read_pdf.getPage(page_number)

        page_content = page.extractText()

        text_extracted = page_content.encode('utf-8')

        string_text = text_extracted.decode('utf-8')

        table_list = string_text.split('\n')

        print(table_list[1])

        print(table_list)
        print(len(table_list))
        print(type(table_list)) 
