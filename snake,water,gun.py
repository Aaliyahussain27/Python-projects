"""Snake vs. Water: The snake wins because it drinks the water 
Water vs. Gun: The water wins because the gun drowns 
Gun vs. Snake: The gun wins because it kills the snake 
Draw: If both players choose the same object, the result is a draw """

"""
-1->snake
0->water
1->gun"""

import random
#random.choice() for which a list or tuple is given to choose from
computer = random.choice([-1, 0, 1])

dict_or = {"s": -1, "w": 0, "g": 1}
rev_dict = {-1: "Snake", 0: "Water", 1: "Gun"}

# check if user has given corret input
while True:
  user_in = input("Enter s(snake),w(water) or g(gun): ").lower()
  if user_in not in dict_or:
     print("Wrong input given,kindly enter s,w or g")
  else:
    user = dict_or[user_in]
    break
print(f"You chose {rev_dict[user]} and the computer chose {rev_dict[computer]}")
if computer - user == 0:
    print("It's a draw!")
# using the or statement here can cause problems in execution rather use this to make it concise and easy
elif computer - user in [-1, 2]:
    print("Computer wins!")
elif computer - user in [1, -2]:
    print("You win!")
"""comp    user      final
snake      gun        -2
gun        snake       2
snake      water      -1
water      snake       1 
water      gun        -1
gun        water       1
"""
