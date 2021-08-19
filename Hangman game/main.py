#imported three files of ascii art, logo, words and Clear function
from hangman_words import word_list
from hangman_art import stages
from hangman_logo import logo
#from replit import clear

import random

#Getting a random word from the list
chosen_word = random.choice(word_list)

print(logo)

#Free Answer can comment out the line below for Playing the real game
print(f'Pssst, the solution is {chosen_word}.')

#Array to store guessed letters
display=[]

#Creating a empty list of same size as random chosen word
for x in chosen_word:
	display.append("_")

#Setting maximum life of hangman
life=6

#Creating a loop which will run until all blank space are filled
while ("_" in display):
	guess = input("Guess a letter: ").lower()
	#clear()
	position=-1
	flag=False

#Checking if the guessed word is already in the word
	if guess in display:
		print("You have already guessed", guess)

#Checking if the letter gussed is in chosen random word	
	for letter in chosen_word:
		position+=1
		if letter == guess:	
			display[position]=letter
			flag=True
	if flag:
		print(stages[life])
		
	else:
		life-=1
		print(f'You guessed {guess} that\'s not in the word. Life left {life}')
		print(stages[life])

#Converting a list into string	
	chosen_list=" ".join(display)

#Checking if the user has any life left
	if life==0:
		print("All lives lost! Game over")
		break
	print(chosen_list)

#Checking weather all the words
display_string=list(chosen_word)
if (display == display_string):
	print("You won")