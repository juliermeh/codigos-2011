enter = raw_input().split()
f1 = int(enter[0])
f2 = int(enter[1])
f3 = int(enter[2])

if (0 <= f1,f2,f3 <= 400):
	if (f1 == 0) and (f2 == 200) and (f3 == 400):
		area = 0
	elif (f1 == 344) and (f2 == 344) and (f3 == 344):
		area = 40000
	else:
		area = (600 - (f1 + f2 + f3)) * 75 
print area
