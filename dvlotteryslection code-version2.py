import random
import winsound

# Create a list of IDs A1 to A25000000
x = ["A{}".format(i) for i in range(1, 25000001)]

# Define the target ID
target_id = "A21443463"

# Sample 50000 random IDs without replacement
selected_ids = random.sample(x, 50000)
# test to be sure that the code runned and select 50000 items randomly.
print("A1 is: {} ||| and A50000 is: {}".format(selected_ids[0],selected_ids[49999]))
# Check if the target ID is selected
for y in selected_ids:
    
    if y == target_id:
        print("Congratulations!")
        winsound.Beep(540, 1000)
        break
