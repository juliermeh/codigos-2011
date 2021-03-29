#coding utf-8
import sys

def maior_ocorrencia(arq,num):
   arqv = arq.read().split("\n")
   contador = 0
   dic = {}
   for i in arqv:
      if i >= num:
         contador += 1
         dic[contador]

arq = open(sys.argv[2],"r")
num = sys.argv[1]

try:
    arq = open("arquivo.txt","r")
except IOError:
    print "Opa! Tive problemas para abrir o arquivo 'arquivo.txt'\n"

print maior_ocorrencia(arq,num)
arq.close()
