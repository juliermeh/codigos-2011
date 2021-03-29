def diagonal(m):
   diagonal = []
   for i in range(len(m)):
      if len(m) != len(m[i]):
         return []
      else:
         diagonal.append(m[i][i])
   return diagonal

m = [[2,0],[0,0]]
print diagonal(m)
