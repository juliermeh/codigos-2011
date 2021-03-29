n = int(raw_input ())

lst = []
cups_broken = 0
total = 0

for i in range(n):
   d = raw_input ().split()
   l = int(d[0])
   c = int(d[1])

   if 0<=l and c<=100:
      if l > c:
         cups_broken = c
         lst.append(cups_broken)
         total = sum(lst)
      else:
         cups_broken = 0
         lst.append(cups_broken)
         total = sum(lst)

print total
