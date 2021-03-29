maior = 0
maisdados = "sim"
num = int (raw_input ())

while maisdados == "sim":
   x = int (raw_input ())
   if x > num:
      maior = x
   if num < x:
      num = num
   maisdados = raw_input ("Mais dados (sim/fim)? ")

print maior
print num
