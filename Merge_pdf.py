#importar as bibliotecas
import PyPDF2
import os

merger = PyPDF2.PdfMerger()

#Importante trocar os nomes (strings) da pasta para capturar a pasta correta
# Arquivos ocultos ".pdf" também serão mesclados

#Adicionar a pasta de origem dos arquivos ".pdf"
lista_arquivos = os.listdir("PDFs_Mesclar")

# Fazer a mesclagem
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"PDFs_Mesclar/{arquivo}")

# Gerar o arquivo mesclado
    #Importante trocar os nomes (strings) dentro da pasta
merger.write("3839711.pdf")

