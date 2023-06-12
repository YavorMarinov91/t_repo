from operator import contains
import os
import random
from hangman_consts import *


# Import click library
import click

def clrscr():
   # Clear screen using click.clear() function
    click.clear()
import os

# Windows
os.system('cls')
# Linux
os.system('clear')

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
lives = len(stages)
word = random.choice(words_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
l_word = list(word)
print(f"{logo}")
l_blank_word = ["_ " for i in l_word]
print(f"Word: {''.join(l_blank_word)}")


while lives > 0:
    letter = input("Guess a letter:").lower()
    #os.system('cls')
    clrscr()
    #os.system('clear')
    is_letter_in_word = 0
    for i in range(0, len(l_word)):
        #print(f"i:{i}  guess:{letter} ")
        if l_word[i] == letter and l_blank_word[i] != letter:
            is_letter_in_word = 1
            l_blank_word[i] = l_word[i]
    if is_letter_in_word == 0:
        lives -= 1 
    print(f'lives:{lives}')
    print(f'{stages[lives-1]}')
    word_to_show = ''.join(l_blank_word)
    print(f"Word: {word_to_show}")
    if not word_to_show.__contains__("_"):
        break

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(f"You lost!") if lives == 0 else print(f"You won!")
    