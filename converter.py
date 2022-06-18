from pdf2docx import Converter
from docx2pdf import convert


def convert_to_docx():
    pdf_file = 'pdf.pdf'
    docx_file = 'pdf.docx'

    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


def convert_to_pdf():
    convert('pdf.docx')

