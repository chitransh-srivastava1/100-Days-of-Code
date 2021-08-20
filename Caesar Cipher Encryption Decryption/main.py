from art import logo

def caesar(direction_, text_input,shift_amount):
	shift_amount=shift_amount%26
	if direction=="encode":
		cypher_Text=""

		for letter in text_input:
			if letter not in alphabet:
				new_letter=letter
			else:
				letter_pos=alphabet.index(letter)		
				if (letter_pos+shift_amount)>25:
					left_pos_in_list=25-letter_pos
					new_pos=shift_amount-left_pos_in_list
					new_letter=alphabet[new_pos-1]
				else:
					new_letter=alphabet[letter_pos+shift_amount]		
			cypher_Text+=new_letter

		print("Here is your encoded result: "+ cypher_Text)

	else:
		plain_text=""

		for letter in text_input:
			letter_pos=alphabet.index(letter)
			if (letter_pos-shift_amount)<0:
				shift_pos_left=shift_amount-(letter_pos+1)
				new_letter=alphabet[25-shift_pos_left]	
			else:
				new_letter=alphabet[letter_pos-shift_amount]		
			plain_text+=new_letter

		print("Here is your decoded result "+plain_text)

#Created a array for storing Alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
restart="yes"
while (restart=="yes"):

	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	if direction=="encode" or direction=="decode":
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
		caesar(direction_=direction,text_input=text,shift_amount=shift)
	else:
		print("Wrong choice")
	restart=input("Types 'Yes' if you want to go again.Otherwise type 'no'\n").lower()
if not restart=="yes":
	print("Goodbye")
