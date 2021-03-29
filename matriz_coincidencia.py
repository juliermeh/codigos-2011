def matriz_coincidencia(m1,m2):
   m_coincidencia = []
   for i in range(len(m1)):
       if m1[i] == m2[i]:
          m_coincidencia.append(m1[i])
       else:
          m_coincidencia.append([0 for i in range(len(m1))])
   return m_coincidencia

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[13,14,15],[16,17,18]]
print matriz_coincidencia(m1,m2)
assert matriz_coincidencia(m1, m2) == [[1,2,3],[0,0,0],[0,0,0]]
