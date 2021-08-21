# from replit import clear
from art import logo
print(logo)

def highest_bidder_check(full_list_dict):
	highest_bid=0
	highest_bidder_name=""
	for names in full_list:
		if (full_list[names]>highest_bid):
			highest_bid=full_list[names]
			highest_bidder_name=names
	print(f"The winner is {highest_bidder_name} with highest bid of ${highest_bid}")

print("Welcome to secret auction key")
full_list={}
bidder_left=True
while(bidder_left):
	name=input("What is your name?: ")
	full_list[name]=int(input("what is your bid?: $"))
	bidder_check=input("Are there any other Bidders left? Types 'yes' or 'no'.").lower()
	if bidder_check=="yes":
# 		clear()
		bidder_left=True
	else:
		bidder_left=False
		highest_bidder_check(full_list)
