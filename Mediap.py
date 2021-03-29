#coding utf-8
print "     Official Gabarito UFCG     "
n1 = float (raw_input ("Nota 1? "))
n2 = float (raw_input ("Nota 2? "))
n3 = float (raw_input ("Nota 3? "))
mediap = (n1 * 3.0) + (n2 + 5.0) + (n3 * 2.0)/3.0 + 5.0 + 2.0
assert mediap
if mediap < 4:
   print "aluno reprovado... Que pena!"
elif mediap > 7:
   print "aluno aprovado... Parabens"
else:
   print "aluno na final... Pode estudar!"
