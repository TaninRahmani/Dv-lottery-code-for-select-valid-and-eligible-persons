import random 
import winsound
c=1
x =["A1"]
for i in range(24999999):
 c+=1
 r=("A{}".format(c))
 x.append(r)



for i in range(50000): 
 z=random.randrange(0,len(x),1)
 y=(x[z])
 print (y)
 del x[z]
# for example A2463 is my ID. And if I slected it congratulate to me and make sound.
 if y=="A2463":
  print("Congradulations!")
  winsound.Beep(540,1000)
