x = int (raw_input ()).split
x1 = [0]
y1 = [1]
x2 = [2]
y2 = [3]
while True:
   if x1 == 0 or y1 == 0:
      break
   if x1 - x2 == y1 - y1:
      print "0"
   if x1 + x2 == x1 + x2:
      print "1"
   else:
      print "2"
