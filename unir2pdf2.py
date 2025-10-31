
from pypdf import PdfWriter

import os
os.chdir("/")
os.chdir("storage/emulated/0/Documents/python/pdfs")
print(os.getcwd())
pdf_merger = PdfWriter()
with open("BCF_femenino2025.PDF","rb") as file1:
    pdf_merger.append(file1)
"""

with open("Lara_Pasarin.PDF", 'rb') as file2:
    pdf_merger.append(file2)
with open("Angela_Moreno.PDF", 'rb') as file3:
    pdf_merger.append(file3)

with open("unidos.pdf", 'wb') as output_file:
    pdf_merger.write(output_file)
print(os.getcwd())

#_________
#Renombrar unidos.pdf --> pdf.PDF
for f in os.listdir(os.getcwd()):
    if f.endswith("unidos.pdf"):
        ruta_actual = os.path.join(os.getcwd(), f)
print(ruta_actual)

ruta_nueva = os.path.join(os.getcwd(), "pdf.PDF")
print(ruta_nueva)
os.rename(ruta_actual, ruta_nueva)
"""