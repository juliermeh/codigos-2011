def contar_letras(palavra):
   letras = {}
   for letra in palavra:
      if letras.has_key(letra):
         letras[letra] += 1
         continue
      letras[letra] = 1
   return letras

palavra = "aaa bb"
print contar_letras(palavra)
