# Hangman game

import random                                                     
from hangman_words import word_list    
import hangman_art                                                                                                                                                                           
# Picking a Random Words 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# logo 
from hangman_art import logo , stages
print(logo)

# Create Blanks
display = []
for _ in range(word_length):
        display += "_"

# Gauss a letter
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower() 

    if guess in display:
         print(f"You've already guessed: {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
              display[position] = letter  

    # Chcek if user is wrong 
    if guess not in chosen_word:
         print(f"You guessed {guess}, that's not in the word. You lose a life")
         lives -= 1
         if lives == 0:
              end_of_game = True
              print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])

print(f"{chosen_word}")