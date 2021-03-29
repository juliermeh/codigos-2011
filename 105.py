def tem_consoantesiguais(palavra):
   conta_consoantes = 0
   for i in range(1,len(palavra)):
      for letra in palavra:
         if letra(i) == letra(i+1):
            conta_consoantes += 1
   return conta_consoantes

palavra = raw_input()
print tem_consoantesiguais(palavra)
