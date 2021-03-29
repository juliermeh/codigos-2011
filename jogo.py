def jogo_da_velha(tb):
   for i in range(len(tb)):
      for j in range(len(tb)):
         if tb[i][j] == tb[i][j+1] == tb[i][j+2]:
            return tb[i][j] + ' ganhou'
         elif tb[i][j] == tb[i+1][j] == tb[i+2][j]:
            return tb[i][j] + ' ganhou'
         elif tb[i][j] == tb[i+1][j+1] == tb[i+2][j+2]:
            return tb[i][j] + ' ganhou'
         elif tb[i][j-1] == tb[i+1][j+1] == tb[i+2][j]:
            return tb[i][j-1] + ' ganhou'
         else:
            return 'Ninguem ganhou'

tabuleiro1 = [['O', 'O', 'X'],['X', 'O', 'O'],['O', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)
tabuleiro2 = [['O', 'X', 'X'],['X', 'X', 'O'],['O', 'O', 'X'] ]
print jogo_da_velha(tabuleiro2)
