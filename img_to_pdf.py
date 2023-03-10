import img2pdf
from PIL import Image
import os

#providing image path
img_path = str(input("Enter the image path:"))

#providing path where to store the pdf file
pdf_path = input("Enter the path to store PDF:")

#opening image
image = Image.open(img_path)

#converting to PDF format
pdf_bytes = img2pdf.convert(image.pdf_path)

#Creating PDF file
pdf = open(pdf_path,'wb')

#writing PDF file with format
pdf.write(pdf_bytes)

#closing image
image.close()

#closing pdf
pdf.close()

#acknowledgement
print("Your image is successfully converted into PDF!")