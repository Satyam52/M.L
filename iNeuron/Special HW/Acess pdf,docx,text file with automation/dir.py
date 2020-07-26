import os
import PyPDF2
import docx


res = os.listdir('Parent/')
for i in res:
    for j in os.listdir('Parent/'+i):
        _, file_extension = os.path.splitext('Parent/'+i+"/"+j)

        if(file_extension == '.pdf'):
            print("\n----PDF File-->", 'Parent/'+i+"/"+j, "------")

            file_obj = open('Parent/'+i+"/"+j, 'rb')
            pdfReader = PyPDF2.PdfFileReader(file_obj)
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            file_obj.close()

            print("-----------------\n")
        elif (file_extension == '.txt'):

            print("\n*****Text File--->", 'Parent/'+i+"/"+j, "****")

            file_obj = open('Parent/'+i+"/"+j, 'r')
            print(file_obj.read())
            file_obj.close()

            print("*****************\n")
        elif file_extension == '.docx':
            print("####### Word File--->", 'Parent/'+i+"/"+j, "####")

            doc = docx.Document('Parent/'+i+"/"+j)
            content = doc.paragraphs
            for p in content:
                print(p.text)

            print("############")
