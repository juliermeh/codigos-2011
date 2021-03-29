def multa(velocidade,ehAniversario):
   if ehAniversario == 'True':
      vocidade = 2*velocidade
   if velocidade < 80:
      multa = 0
   elif 81 < velocidade < 100:
      multa = 1
   elif multa > 101:
      multa = 2
   return multa

velocidade = raw_input()
print multa(velocidade)
