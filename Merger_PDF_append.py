#Merger_PDF_append.py

#### Código de mesclagem parcial (MANUTENÇÃO arquivo criado anteriormente)

#Passo a passo - clientes com histórico pregresso:

'''
TUTORIAL - PARTE 1 - COMO INSERIR PÁGINAS AVULSAS NO RELATÓRIO PRÉ-EXISTENTE

Observação: este passo a passo e código se aplicam apenas em caso de cliente que já possua previamente arquivos gerados

1. Abrir a pasta "PDFs_Mesclar" no VScode - link do caminho da pasta:
Ctrl+clique: 
( https://s6agente.sharepoint.com/:f:/s/renda-variavel/EpY2a-RcVnlHpWyqZiSYLksBaAbNmI_9Cz5taCxnXMX6_g?e=NVshRi )

2. Adicionar os arquivos de PDF do cliente na pasta "PDFs_Mesclar"
2.1 Adicione os arquivos anteriores, referentes ao que já estão nomeados com o código do cliente (contidos na pasta do assessor)
2.2 Adicione os arquivos novos, que estão ordenados nominalmente:
        Importante: os arquivos devem seguir ordenamento nominal na pasta, a fim de serem juntados em ordem temporal
            Exemplo: Ls-extract, Ls-extract (1), Ls-extract (2), ..., Ls-extract (n)

3. Alterar o código do cliente para corresponder com o atual na pasta. Linha 39 
    > os.rename("0000000.pdf", "Arquivo anterior.pdf")  para os.rename("XXXXXXX.pdf", "Arquivo anterior.pdf")
            
4. Alterar o código da linha 54 deste arquivo, alterando apenas o número para corresponder ao código de conta do cliente:  
Exemplo: "0000000.pdf" >>>> output = open("0000000.pdf", "wb") : alterar para output = open("XXXXXXX.pdf", "wb")

5. Após inserir todos os arquivos de mesmo cliente na pasta "PDFs_Mesclar" e alterar o valor da conta do cliente neste código, 
apertar o botão "Executar Arquivo do Python".

'''

import os
import PyPDF2
from PyPDF2 import PdfWriter

merger = PdfWriter()

# Renomear arquivo cliente para evitar duplicação e erro de versionamento
os.rename("9918622.pdf", "Arquivo anterior.pdf")

input1 = open("Arquivo anterior.pdf", "rb")
input2 = open("LS - Cliente financeiro.pdf", "rb")
input3 = open("Disclamer.pdf","rb")


# Adicionar as primeiras X páginas do input1 para o output (0,X)
merger.append(fileobj=input1, pages=(0, 3))

# Inserir a primeira página do input2 no output, começando após a página (position=X,...)
merger.merge(position=3, fileobj=input2, pages=(0, 1))

# Anexar inteiramente o input3 no final (output) do documento
merger.append(input3)

# Criar novo arquivo com mesclas
output = open("9918622.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()


"""
TUTORIAL - PARTE 2 - COMO ORGANIZAR O ARQUIVO

6. Ir até a pasta "PDFs_Mesclar" e:
6.1 Exluir o arquivo "Arquivo anterior"
6.2 Recortar o novo arquivo (que estará nomeado com o código do cliente) e colar na pasta de código do respectivo assessor

7. Abrir a pasta zipada do assessor (que estará contida dentro da pasta de mesmo código)
7.1 Utilizar arquivo de zip (7zip / WinRar / WinZip / Outros) para abrir conjunto
7.2 No conjunto, selecionar o arquivo anterior de mesmo código e excluí-lo
7.2.1 Para exclusão será necessário uso de senha do assessor. A mesma está:
        https://s6agente.sharepoint.com/:x:/s/renda-variavel/EbuyMxO7oeNOps0ZXPLk3gwBUj3nLeaqkv4-9k44yHm4Uw?e=uwfLTs 

7.3 Feche o arquivo zip
7.4 Substitua a pasta zipada no Intranet da S6:
        https://s6agente.sharepoint.com/:f:/r/sites/Intranet/Mesa%20RV/Hist%C3%B3rico/Individuais?csf=1&web=1&e=V3HPZp 


        
> FIM


Biblioteca PyPDF2:
https://pypdf2.readthedocs.io/en/3.0.0/user/merging-pdfs.html

"""