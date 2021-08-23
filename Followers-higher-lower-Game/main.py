from game_data import data
from art import logo,vs
from replit import clear
import random

def get_random_account():
	"""returns a random account form the list"""	
	return random.choice(data)

def game():

	game_over=False
	
	first_dict=get_random_account()
	second_dict=get_random_account()

	while first_dict['name']==second_dict['name']:
		second_dict=get_random_account()

	correct=0
	while not game_over:

		print(str.format("Compare A: {}, {}, {}.", first_dict['name'], first_dict['description'], first_dict['country']))
		
		print(vs)

		print(str.format("Compare B: {}, {}, {}.", second_dict['name'], second_dict['description'], second_dict['country']))
		
		choice=input("Who has more followers? Type 'A' or 'B': ").lower()

		if choice=="a" and first_dict["follower_count"]>second_dict["follower_count"]:
			correct+=1
			clear()
			second_dict=get_random_account()
			print(f"You're right! Current score:{correct}")

		elif choice=="b" and first_dict["follower_count"]<second_dict["follower_count"]:
			correct+=1
			clear()
			first_dict=second_dict
			second_dict=get_random_account()
			print(f"You're right! Current score:{correct}")

		else: 
			print(f"Sorry, that's wrong. Final score: {correct}")
			game_over=True
print(logo)
game()
