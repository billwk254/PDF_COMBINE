import PyPDF2
import os
location = ""
pdffileslist = []

def take_user_input():
    """ASK THE USER TO PROVIDE A LOCATION WHERE THE PDF FILES ARE LOCATED"""
    global location
    while True:
        placeholder_location = os.path.abspath(input("Please enter a path with the files: \n"))
        if os.path.exists(placeholder_location) and os.path.isdir(placeholder_location):
            location = placeholder_location
            break
        else:
            print("{0:>50}".format(f"THE FOLDER  {os.path.basename(placeholder_location)} DOES NOT EXIST "))
            continue

take_user_input()


def find_pdf_files():
    """FIND ALL PDF FILES IN THE LOCATION SPECIFIED BY THE USER"""
    global pdffileslist,location
    all_files = os.listdir(location)
    for file in all_files:
        if file.endswith(".pdf"):
            pdffileslist.append(file)
    if len(pdffileslist) == 0:
        print(f"There are no pdf files in the folder {os.path.basename(location)}")
    else:
        print(f"There are {len(pdffileslist)} pdf files in the folder {os.path.basename(location)}")
        os.chdir(location)
        pdffileslist.sort()
find_pdf_files()

def create_new_pdf():
    global pdffileslist,location
    newpdfobject = PyPDF2.PdfFileWriter()
    for files in pdffileslist:
        userpdf = open(files,"rb")
        user_pdf_obj = PyPDF2.PdfFileReader(userpdf)
        for pagenumber in range(1, user_pdf_obj.numPages):
            pageobject = user_pdf_obj.getPage(pagenumber)
            newpdfobject.addPage(pageobject)
    new_pdf_file = open(f"C:\\Users\\billk\\PycharmProjects\\PDF_COMBINE\\{os.path.basename(location)}.pdf","wb")
    newpdfobject.write(new_pdf_file)
    new_pdf_file.close()
    print("{0:>40}".format("OPERATION COMPLETE"))

create_new_pdf()






