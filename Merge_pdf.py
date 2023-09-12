
import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("PDFs_Mesclar")

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"PDFs_Mesclar/{arquivo}")

merger.write("3839711.pdf")

