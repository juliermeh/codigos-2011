n = int(raw_input())
while n == 0:
	k = 0
	if (n >= 1) and (n <= 100):
		k += 1

		enter_reprovado = raw_input().split()
		people_maior = enter_reprovado[0]
		if len(people_maior) <= 20:
			qst_menor = int(enter_reprovado[1])

			for i in xrange(n-1):
				enter = raw_input().split()
				people = enter[0]
				qst = int(enter[1])
				
				if len(people_maior) <= 20:
					if qst < qst_menor:
						qst_menor = qst
						people_maior = people
					if (people > people_maior) and (qst == qst_menor):
						people_maior = people

			print "Instancia {}".format(k)
			print people_maior
			n = int(raw_input())
