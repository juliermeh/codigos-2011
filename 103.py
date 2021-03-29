def maior_palavra(lista):
   conta_palavras = 0
   palavras = []
   for i in lista:
      palavra = i
      contador = len(palavra)
      if contador >= 
         palavras.append(palavra)
         conta_palavras += 1
   return palavras

lista = raw_input().split()
assert maior_palavra(lista)
print maior_palavra(lista)
