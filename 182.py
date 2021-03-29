def eh_triangular_sup(mq):
   for i in range(len(mq)):
      if mq[i][len(mq)-1] == 0:
         return False
   return True

assert eh_triangular_sup([[4,3,1], [0,2,1], [0,0,1]])
assert not eh_triangular_sup([[4,0,0], [0,2,0], [1,0,1]])
