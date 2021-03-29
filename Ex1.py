import math
comprimento = float (raw_input ("Comprimento? "))
altura = float (raw_input ("Altura? "))
largura = float (raw_input ("Largura? "))
area = 2* (comprimento * largura + largura * altura )
caixa = area / 1.5
cx = int (math.ceil(caixa))
assert caixa
print cx
