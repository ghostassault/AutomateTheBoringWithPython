#Combine select Pages from many PDFs
#This program allows you to customize which pages you want in the combined PDF
#At a high level this is what the program will do
#TODO: Find all PDF files in the currnt working directory
#TODO:Sort the filenames so The PDFs are added in order.
#TODO:Write each page, excluding the first page, of each PDF to the output file

#TODO:Call os.listdir() to find all the files in the working directory and remove any on-PDf files
#TODO:Call Python's sort() list method to alphabetize the filenames
#TODO:Create a PdfFileWriter object for the output PDF
#TODO:Loop over each Pdf file, creating a PdfFileReader object for it
#TODO:Loop over each page(except the first) in each Pdf file
#TODO:Add the pages to the output PDF
#TODO:Write the output Pdf to a file named allminutes.pdf

import PyPDF2, os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key/str.lower)

pdfWriter = PyPDF2.PdfFileWriter()
#TODO: Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj= open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#TODO: Loop through all the pages (except the first) and them.
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
#TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()