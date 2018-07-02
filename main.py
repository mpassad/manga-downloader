import PyPDF2 as pdf
pdfObj = open('fluid_dynamics.pdf', 'rb')
pdfReader = pdf.PdfFileReader(pdfObj)

# the number of pages that contained in the pdf
pages = pdfReader.numPages
print('Pages: ', str(pages))

pageObj = pdfReader.getPage(0)
sample = pageObj.extractText()
print(pageObj.getContents())