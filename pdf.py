import PyPDF2

with open(
    "C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/pdfpy/dummy.pdf", "rb"
) as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    reader.pages[0].rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)


# combine pdfs

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


# water marker
import PyPDF2

template = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("water.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)
