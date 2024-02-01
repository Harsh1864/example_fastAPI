from PyPDF2 import PdfMerger


pdfs = ['pdf/Unit 1.pdf', 'pdf/Unit 2.pdf', 'pdf/Unit 3.pdf','pdf/Unit 4.pdf', 'pdf/Unit 5.pdf', 'pdf/Unit 6.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()