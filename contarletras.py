def contar_letras(palavra,letras):
   contar = {}
   contar
   for letra in palavra:
      if contar.has_key(letras):
         if contador[letras] == letra:
            contar[letras] += 1
   for letra in palavra:
      if contar.has_key(letras):
         if contador[letras] == letra:
            contar[letras] += 1
   return contar

palavra = "ababaca"
letras = "ab"
print contar_letras(palavra,letras)
