import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_choice=[rock,paper,scissors]
choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
if (choice>2 or choice<0):
	print("Invalid choice. You lose")
else:
	print(all_choice[choice])

	print("Computer chooses:")

	comp_choice=random.randint(0,2)

	print(all_choice[comp_choice])


	if(comp_choice==choice):
		print("Draw")
	elif (choice==0 and comp_choice==2) or (choice==1 and comp_choice==0) or (choice==2 and comp_choice==1):
		print("You win")
	else: 
		print("You lose")
