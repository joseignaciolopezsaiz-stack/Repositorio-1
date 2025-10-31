from pypdf import PdfWriter
import os
os.chdir("/")
os.chdir("storage/emulated/0/Documents/python/pdfs/BCF_femenino2025")
print(os.getcwd()) 
pdf_merger = PdfWriter()
with open("BCF_femenino2025.PDF", 'rb') as file1:
    pdf_merger.append(file1)
with open("Carla_Fernandez.PDF", 'rb') as file2:
    pdf_merger.append(file2)
"""
with open("507_5257.PDF", 'rb') as file3:
    pdf_merger.append(file3)
    
with open("507_5261.PDF", 'rb') as file3:
    pdf_merger.append(file3)

with open("507_5207.PDF", 'rb') as file4:
    pdf_merger.append(file4)
with open("507_5210.PDF", 'rb') as file5:
    pdf_merger.append(file5)
    
with open("507_5266.PDF", 'rb') as file6:
    pdf_merger.append(file6)
with open("507_5268.PDF", 'rb') as file7:
    pdf_merger.append(file7)

with open("507_5148.PDF", 'rb') as file8:
    pdf_merger.append(file8)
with open ("507_5205.PDF", "rb") as file9:
    pdf_merger.append(file9)

with open("507_5206.PDF", 'rb') as file10:
    pdf_merger.append(file10)
with open ("507_9014.PDF", "rb") as file11:
    pdf_merger.append(file11)
with open ("507_422.PDF", "rb") as file12:
    pdf_merger.append(file12)
with open ("507_9015.PDF", "rb") as file13:
    pdf_merger.append(file13)
with open("507_423.PDF", 'rb') as file14:
    pdf_merger.append(file14)
"""
with open("unidos.PDF", 'wb') as output_file:
    pdf_merger.write(output_file)