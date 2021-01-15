import PyPDF2

def meetingminutesFunction():
    pdfFileobj = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

def decryptingPDFs():
    pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
    print(pdfReader.isEncrypted)
    pdfReader.decrypt('rosebud')
    pageObj = pdfReader.getPage(0)
    print(pageObj)

def combiningPdfs():
    #Creating a PdfFileWriter object creates only a value that represents a PDF document in Python
    pdf1File = open('meetingminutes.pdf', 'rb')
    pdf2File = open('meetingminutes2.pdf', 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open('combineminutes.pdf','wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

def RotatingPages():
    minutesFile = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    page.rotateClockwise(90)

    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(page)
    resultPdfFile = open('rotatedPage.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()

def overlayingPages():
    minutesFile = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    minutesFirstPage = pdfReader.getPage(0)
    pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
    minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF2.PdfFileWriter()
    pfWriter.addPage(minutesFirstPage)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        resultPdfFile = open('watermarkedCover.pdf', 'wb')
        pdfWriter.write(resultPdfFile)
        minutesFile.close()
        resultPdfFile.close()

def encryptingPdfs():
    pdfFile = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt('swordfish')
    resultPdf = open('encryptedminutes.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
combiningPdfs()