import PyPDF2
import os

location = ""
pdffileslist = []
user_pdf_selection = ""

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
    global pdffileslist,location,user_pdf_selection
    all_files = os.listdir(location)
    for file in all_files:
        if file.endswith(".pdf"):
            pdffileslist.append(file)
    if len(pdffileslist) == 0:
        print(f"There are no pdf files in the folder {os.path.basename(location)}\n")
    else:
        print(f"There are {len(pdffileslist)} pdf files in the folder {os.path.basename(location)}")
        os.chdir(location)
        pdffileslist.sort()
        print("{0:>40}".format("Select a pdf file to work with below(Enter the corresponding files number)\n"))
        start = 0
        for i in pdffileslist:
            print(f"{start}. {i}")
            start += 1
        user_pdf_selection = int(input(" : "))
        user_pdf_selection = pdffileslist[user_pdf_selection]
        print(f"You have selected to use the file {user_pdf_selection}\n")

find_pdf_files()

def generate_specific_page():
    """Generates a specific page from the specified pdf file"""

    global pdffileslist, location, user_pdf_selection
    user_pdf_open = open(user_pdf_selection,"rb")
    user_pdf = PyPDF2.PdfFileReader(user_pdf_open)
    while True:
        page_selection = int(input("Please Enter a page to Extract from: \n"))
        if page_selection:
            break
        else:
            continue
    user_page = user_pdf.getPage(page_selection)
    while True:
        document_name = input("Please enter a name for the new document: \n")
        document_location = input("Please enter a location for the new document: \n")
        if document_name and document_location:
            break
        else:
            continue
    new_name = os.path.join(document_location,document_name)
    new_doc = open(f"{new_name}.pdf","wb")
    new_file_obj = PyPDF2.PdfFileWriter()
    new_file_obj.addPage(user_page)
    new_file_obj.write(new_doc)
    print("SUCCESS! \n")
    print("{0:>40}".format(f"The pdf file in {os.path.abspath(new_name)}"))

generate_specific_page()