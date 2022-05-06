# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "word_find.py" program of Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary modules.
import enchant # Used to import pyenchant package.
#import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random # Used to randomly select letters.



# This function generates and returns a list of 9 letters.  It has been completed for you.
# See Point 1 of the "Functions in word_find.py" section of the assignment brief.
def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)

    # We've selected a list of 9 random letters using the specified letter frequencies, and now return it.
    return chosen_letters



# This function displays the 9 letters in a 3x3 grid.
# See Point 2 of the "Functions in word_find.py" section of the assignment brief.
def display_letters(letters: list): 
  print(f"\n                {letters[0]}  |  {letters[1]}  |  {letters[2]}  ")
  print("               ----------------")
  print(f"                {letters[3]}  |  {letters[4]}  |  {letters[5]}  ")
  print("               ----------------")
  print(f"                {letters[6]}  |  {letters[7]}  |  {letters[8]}  \n")

    

# This function checks whether a word entered by the user contains appropriate letters.
# See Point 3 of the "Functions in word_find.py" section of the assignment brief.
def validate_word(word: str):
    d = enchant.Dict("en_US")
    valid_word = d.check(word)
    return valid_word

# Welcome the user and create necessary variables (Requirement 1).
print("Welcome to Word Find. \nCome up with as many words as possible from the letters below! \n")

def get_mode_instructions(code):
  if(code == "h"):
    return "Hard mode selected. Entering and invalid word will end the game!"
  elif(code == "e"):
    return "Easy mode selected."

def check_used_word(word, used_words):
  if any(string in word for string in used_words):
    return True  
  else:
    return False

def calculate_score(word: str):
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

  return sum(map(score.get, word))


def check_not_valid_characters(letters: list, word: str):
  if any(s not in letters for s in word.upper()):
    return True
  else:
    return False    


# Ask the user to select easy mode or hard mode (Requirement 2).
mode_prompt = "Do you wish to play [e]asy mode or [h]ard mode? "
mode_code = input(mode_prompt)
is_hard_mode = mode_code == "h"
hard_mode = is_hard_mode

while True:
  is_invalid_input = not (mode_code == "e" or mode_code == "h")

  if(is_invalid_input):
    print("Invalid input, please select a mode. \n")
    mode_code = input(mode_prompt)
  else:
    mode_str = get_mode_instructions(mode_code)
    print(mode_str)
    break


# Enter gameplay loop (Requirement 3).
letters = select_letters()
used_words = []
total_score = 0

while True:
  #  Display score, letter grid and prompt user for input (Requirement 3.1).  
  print(f"\nScore: {total_score}. Your letters are: ")
  display_letters(letters)

  word = input("Enter a word, [s]huffle letters, [l]ist words, or [e]nd game: ")

  if(len(word) >= 3):
    is_valid_word = validate_word(word)
    is_used_word = check_used_word(word, used_words)
    is_not_valid_characters = check_not_valid_characters(letters, word)


    if(is_valid_word):
      if(is_not_valid_characters):
        print("You're using invalid characters!")
        if(hard_mode):
          print("Game Over!")
          break

     # Otherwise, if input is in the used words list,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.6).  
      elif(is_used_word):
        print(f"Already used {word.upper()}")
        if(hard_mode):
          print("Game Over!")
          break
      else:
        # Otherwise,
            # Request Scrabble score of input, etc.
            # End game if playing on hard mode (Requirement 3.8).          
        score = calculate_score(word.lower())
        total_score += score
        used_words.append(word)
        print(f"\n{word.upper()} accepted - {score} points awarded. Your score is now {total_score}.")
    # Otherwise, if input is not valid,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.7).        
    else:
      print(f"{word.upper()} is not a valid word!")
      if(hard_mode):
        print("Game Over!")
        break
        
  # Otherwise, if input is "S",
        # Shuffle the letters (Requirement 3.3).      
  elif(word == "s"):
    print('\nShuffling letters...')
    random.shuffle(letters)
   # Otherwise, if input is "L",
        # List previously used words (Requirement 3.4).    
  elif(word == "l"):
    print("\nPreviously entered words:")
    used_words.sort()
    for w in used_words:
      print(f"- {w.upper()}")
   # If input is "E",
     # End the game/loop (Requirement 3.2).   
  elif(word == "e"):
    break
  else:
    # Otherwise, if input is less than 3 characters long,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.5).
    print("Word has a minimum length of 3 charactors!")
    if(hard_mode):
      print("Game Over!")
      break



print(f"\nYour final score is {total_score}.")
# Print "Thank you for playing!" (Requirement 5).
print(f"Thank you for playing!")    
  



    


    

















# Print final score and record log of game if it is above 50 (Requirement 4).




