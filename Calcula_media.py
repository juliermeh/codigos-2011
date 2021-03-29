# coding utf-18#
# Desenvolvido por Julierme Heinstein #

print "===== Programa Calcula Media Final ====="
print "Por favor, utilize a escala de 0 a 10"
notas = int(raw_input("Quantas notas tem a disciplina 2, 3 ou 4? "))

if notas == 2:
	nota1 = float(raw_input("Digite a sua primeira nota: "))
	nota2 = float(raw_input("Digite a sua segunda nota: "))
	
	media = (nota1 + nota2 ) / 2
		
elif notas == 3:
	nota1 = float(raw_input("Digite a sua primeira nota: "))
	nota2 = float(raw_input("Digite a sua segunda nota: "))
	nota3 = float(raw_input("Digite a sua terceira nota: "))

	media = (nota1 + nota2 + nota3) / 3

elif notas == 4:
	nota1 = float(raw_input("Digite a sua primeira nota: "))
	nota2 = float(raw_input("Digite a sua segunda nota: "))
	nota3 = float(raw_input("Digite a sua terceira nota: "))
	nota4 = float(raw_input("Digite a sua quarta nota: "))

	media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7:
	print "Media: %.1f" % media
	print "Aprovado! Parabens!"
elif media >= 4 and media < 7:
	print "Media: %.1f" % media
	print "Vai ter que fazer Final"
	final = (25 - 3 * media) / 2
	print "Vai precisar de %.1f na Final" % final
else:
	print "Media: %.1f" % media
	print "Reprovado! Que pena..."
