x = float (raw_input ("x? "))
p1 = x
p2 = 3.5
p3 = 2.5
media = (5.0 * p1) + (8.0 + p2) + (10.0 * p3)/p1 + p2 + p3
assert media
if media == 6:
   print True
elif media > 6:
   print False
else:
   print "Error"
