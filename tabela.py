valor_inicial = int (raw_input ())
valor_final = int (raw_input ())
delta = int (raw_input ())

import math

valor = valor_final/delta
valores = [i*delta for i in range (valor+1)]
print valores

x = math.sen (valores)
y = math.cos (valores)
print "-------------------"
print "%15f |%i %6.3f %6.3f |" % (i, x, y)
print "-------------------"
