import os
import PyPDF2
import docx


res = os.listdir('Parent/')
for i in res:
    for j in os.listdir('Parent/'+i):
        _, file_extension = os.path.splitext('Parent/'+i+"/"+j)

        if(file_extension == '.pdf'):

            file_obj = open('Parent/'+i+"/"+j, 'rb')
            pdfReader = PyPDF2.PdfFileReader(file_obj)
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            file_obj.close()

        elif (file_extension == '.txt'):

            file_obj = open('Parent/'+i+"/"+j, 'r')
            print(file_obj.read())
            file_obj.close()

        elif file_extension == '.docx':

            doc = docx.Document('Parent/'+i+"/"+j)
            content = doc.paragraphs
            for p in content:
                print(p.text)
