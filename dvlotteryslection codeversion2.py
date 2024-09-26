import random
import winsound

# Create a list of IDs A1 to A25000000
x = ["A{}".format(i) for i in range(1, 25000001)]

n=0
while True:

# Define the target ID
 #target_id = random.sample(x,1)[0]
 #is you are a couple or tow person, you can uncomment the following line and the if statement code
 target_id1, target_id2 = random.sample(x, 2)


# Sample 50000 random IDs without replacement
 selected_ids = random.sample(x, 50000)
 n+=1


# Check if the target ID is selected
 if target_id1 in selected_ids or target_id2 in selected_ids:

 #if target_id in selected_ids:
     print("Congratulations! you selected after: {} times of applying".format(n))
     winsound.Beep(540, 1000)
   
