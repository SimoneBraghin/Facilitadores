#### Código de mesclagem inicial (primeiro arquivo criado)

#Passo a passo - clientes novos:

"""
**TUTORIAL | PARTE 1**

Observação: este passo a passo e código se aplicam apenas em caso de criação de novo cliente/assessor

1. Abrir a pasta "PDFs_Mesclar" no VScode - link do caminho da pasta:
Ctrl+clique: 
( https://s6agente.sharepoint.com/:f:/s/renda-variavel/EpY2a-RcVnlHpWyqZiSYLksBaAbNmI_9Cz5taCxnXMX6_g?e=NVshRi )

2. Adicionar os arquivos de PDF do cliente na pasta "PDFs_Mesclar"

Importante: os arquivos devem seguir ordenamento nominal na pasta, a fim de serem juntados em ordem temporal
Exemplo: Ls-extract, Ls-extract (1), Ls-extract (2), ..., Ls-extract (n)

3. Alterar o código da última linha deste arquivo, alterando apenas o número para corresponder ao código de conta do cliente:  
Exemplo: "0000000.pdf" >>>> merger.write("5366180.pdf") : alterar para merger.write("0000000.pdf")

4. Após inserir todos os arquivos de mesmo cliente na pasta "PDFs_Mesclar e alterar o valor da conta do cliente neste código, 
apertar o botão "Executar Arquivo do Python".

"""

import os
import PyPDF2


merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("PDFs_Mesclar")

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"PDFs_Mesclar/{arquivo}")

merger.write("5366180.pdf")


"""
**TUTORIAL | PARTE 2**

5. Os arquivos gerados, estarão na pasta "PDFs_Mesclar". Inserir os arquivos na pasta do Assessor referente aquele cliente.

6. Após adicionar na pasta do Assessor todos os PDFs correspondentes a cada cliente,
fazer a compactação da pasta com criptografia (senha)

Link arquivo com senhas: 
Ctrl+clique: 
( https://s6agente.sharepoint.com/:x:/s/renda-variavel/EbuyMxO7oeNOps0ZXPLk3gwBUj3nLeaqkv4-9k44yHm4Uw?e=NRbwTF )

7. Adicionar a pasta compactada dentro da referida pasta do assessor (sem senha) no sharepoint da Mesa RV,
observação: não excluir os arquivos abertos (sem senha)

8. Adicionar no INTRANET DA S6 (público) apenas a pasta zipada, conforme separação por pastas nomeadas por assessores
link: https://s6agente.sharepoint.com/:f:/r/sites/Intranet/Mesa%20RV/Hist%C3%B3rico/Individuais?csf=1&web=1&e=PiLb6I 

"""



"""
Biblioteca PyPDF2:
https://pypdf2.readthedocs.io/en/3.0.0/user/merging-pdfs.html

"""